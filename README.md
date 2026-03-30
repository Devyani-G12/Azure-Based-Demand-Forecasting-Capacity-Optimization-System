## Azure-Based Demand Forecasting & Capacity Optimization System
About the Project

This project focuses on analyzing Azure infrastructure usage data and predicting future demand. The main idea is to understand how resources are being used and use that information to support better capacity planning with the help of machine learning and some automation.

## Dataset

The dataset contains the following fields:

Timestamp
Region
CPU usage
Memory usage
Disk and network activity
VM configuration
Cost and utilization
External factors like GDP growth and electricity price

##  Tech Stack
Python
Pandas, NumPy
Scikit-learn
XGBoost

##  Data Cleaning

The data was cleaned and prepared before using it for modeling. The main steps were:

Converted timestamp into datetime format for time-based analysis
Sorted the data properly for time series usage
Handled missing values (numeric values using interpolation and categorical using mode)
Fixed region naming to keep it consistent
Removed duplicate records

Output file: azure_cleaned_dataset.csv

## Feature Engineering

Some additional features were created to improve model performance:

Time-based features like hour, day_of_week, and is_weekend
Lag features to capture previous demand values (target_lag_1, target_lag_24)
Rolling mean to understand short-term trends
Spike flag to detect sudden increases in demand
One-hot encoding for categorical columns like region, vm_type, and cloud_provider

Output file: feature_eng_dataset.csv

## Model Training

Two different models were used in this project:

ARIMA (for time-series forecasting)
XGBoost (machine learning model)

Hyperparameter tuning was done using GridSearchCV to improve performance.

##  Model Evaluation

The models were evaluated using:

Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
Bias

These metrics helped in checking how close the predictions are to actual values.

## Results
ARIMA
MAE: 15.75
RMSE: 19.97
Bias: -12.83
XGBoost
MAE: 3.95
RMSE: 6.00
Bias: 0.23

XGBoost gave better results compared to ARIMA, so it was selected as the final model.

Endpoint: /predict
Takes input features
Returns predicted demand
Batch Prediction

A script (predict.py) is used to generate predictions and save them into:

forecast_output.csv

The model is updated only if the new one performs better
Final Outputs
Cleaned dataset: azure_cleaned_dataset.csv
Feature dataset: feature_eng_dataset.csv
Forecast output: forecast_output.csv
Model file: model.pkl
##  Conclusion

This project builds a complete pipeline starting from data cleaning to prediction, deployment, and monitoring. It helps in understanding demand patterns and can be useful for better resource planning in cloud systems.
