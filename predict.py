import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import mean_squared_error

model = joblib.load("C:/Users/gorak/OneDrive/Desktop/azure/model/model.pkl")

df = pd.read_csv("C:/Users/gorak/OneDrive/Desktop/azure/feature_eng_dataset.csv")

X = df.drop(["target","timestamp"], axis=1)

df["forecast"] = model.predict(X)

# add region + service type (example columns)
df["region"] = "asia-south"
df["service_type"] = "Standard_D4s_v3"

df[["timestamp","target","forecast","region","service_type"]].to_csv("forecast_output.csv", index=False)

print("Forecast file created")

# ---------------- MONITORING ----------------
rmse = np.sqrt(mean_squared_error(df["target"], df["forecast"]))
print("RMSE:", rmse)

# ---------------- ALERT ----------------
if rmse > 10:
    print("ALERT: Model performance degraded")