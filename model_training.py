import pandas as pd
import numpy as np

from statsmodels.tsa.arima.model import ARIMA
from xgboost import XGBRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import GridSearchCV


# ---------------- LOAD DATA ----------------

df = pd.read_csv("feature_eng_dataset.csv")

# convert timestamp and sort for time series
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")


# split dataset (80% train, 20% test)
train_size = int(len(df) * 0.8)

train = df[:train_size]
test = df[train_size:]


# ---------------- ARIMA MODEL ----------------

# ARIMA uses only the target column
arima_model = ARIMA(train["target"], order=(5,1,0))

arima_fit = arima_model.fit()

arima_predictions = arima_fit.forecast(steps=len(test))


# ---------------- XGBOOST MODEL ----------------

# prepare features and target
X_train = train.drop(["target","timestamp"], axis=1)
y_train = train["target"]

X_test = test.drop(["target","timestamp"], axis=1)
y_test = test["target"]

# create model
xgb_model = XGBRegressor(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.05
)

# train model
xgb_model.fit(X_train, y_train)

# predictions
xgb_predictions = xgb_model.predict(X_test)


# ---------------- EVALUATION FUNCTION ----------------

def evaluate(actual, predicted):

    mae = mean_absolute_error(actual, predicted)

    rmse = np.sqrt(mean_squared_error(actual, predicted))

    bias = np.mean(predicted - actual)

    return mae, rmse, bias


# ---------------- MODEL COMPARISON ----------------

arima_mae, arima_rmse, arima_bias = evaluate(test["target"], arima_predictions)

xgb_mae, xgb_rmse, xgb_bias = evaluate(y_test, xgb_predictions)


print("\nARIMA Results")
print("MAE:", arima_mae)
print("RMSE:", arima_rmse)
print("Bias:", arima_bias)


print("\nXGBoost Results")
print("MAE:", xgb_mae)
print("RMSE:", xgb_rmse)
print("Bias:", xgb_bias)


# ---------------- MODEL TUNING ----------------

param_grid = {
    "n_estimators":[100,200],
    "max_depth":[4,6,8],
    "learning_rate":[0.01,0.05,0.1]
}

grid_search = GridSearchCV(
    XGBRegressor(),
    param_grid,
    cv=3,
    scoring="neg_mean_absolute_error"
)

grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_

print("\nBest Parameters:", grid_search.best_params_)


# evaluate tuned model
tuned_predictions = best_model.predict(X_test)

tuned_mae, tuned_rmse, tuned_bias = evaluate(y_test, tuned_predictions)

print("\nTuned XGBoost Results")
print("MAE:", tuned_mae)
print("RMSE:", tuned_rmse)
print("Bias:", tuned_bias)


# ---------------- BACKTESTING ----------------

errors = []

# rolling validation
for i in range(500, len(df)-1):

    train_bt = df[:i]
    test_bt = df[i:i+1]

    X_train_bt = train_bt.drop(["target","timestamp"], axis=1)
    y_train_bt = train_bt["target"]

    X_test_bt = test_bt.drop(["target","timestamp"], axis=1)
    y_test_bt = test_bt["target"]

    model_bt = XGBRegressor(n_estimators=200, max_depth=6)

    model_bt.fit(X_train_bt, y_train_bt)

    pred_bt = model_bt.predict(X_test_bt)

    error = mean_absolute_error(y_test_bt, pred_bt)

    errors.append(error)

print("\nAverage Backtesting MAE:", np.mean(errors))


# ---------------- FINAL MODEL SELECTION ----------------

print("\nFinal Model Selection")

if tuned_mae < arima_mae:
    print("XGBoost selected as final model")
else:
    print("ARIMA selected as final model")