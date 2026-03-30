# Azure-Based-Demand-Forecasting-Capacity-Optimization-System

## About the Project
This project focuses on analyzing Azure infrastructure usage data and predicting future demand. The main goal is to support capacity planning using machine learning and automation.

---

## Dataset
The dataset includes:
- timestamp  
- region  
- cpu usage  
- memory usage  
- disk and network activity  
- VM configuration  
- cost and utilization  
- external factors like GDP growth and electricity price  

---

## Data Cleaning
The data was cleaned using the following steps:
- Converted timestamp into datetime format  
- Sorted data for time series  
- Handled missing values (numeric → interpolation, categorical → mode)  
- Standardized region names  
- Removed duplicate records  

### Output:
- `azure_cleaned_dataset.csv`

---

## Feature Engineering
New features were created to improve model performance:
- Time features: hour, day_of_week, is_weekend  
- Lag features: previous demand values (target_lag_1, target_lag_24)  
- Rolling mean to capture short-term trends  
- Spike flag to detect sudden increases  
- One-hot encoding for region, vm_type, and cloud_provider  

### Output:
- `feature_eng_dataset.csv`

---

## Model Training
Two models were used:
- ARIMA (time series model)  
- XGBoost (machine learning model)  

Evaluation metrics:
- MAE  
- RMSE  
- Bias  

Hyperparameter tuning was done using GridSearchCV.

XGBoost performed better, so it was selected as the final model.

---

## Model Results

### ARIMA
- MAE: 15.75  
- RMSE: 19.97  
- Bias: -12.83  

### XGBoost
- MAE: 3.95  
- RMSE: 6.00  
- Bias: 0.23  

---

## API (Real-Time Prediction)
The model is deployed using Flask API.

- Endpoint: `/predict`  
- Accepts input features  
- Returns predicted demand  

---

## Batch Prediction
A script (`predict.py`) is used to generate predictions and save them into:
- `forecast_output.csv`

---

## Dashboard
The forecast data is used to create dashboards (Excel / Power BI) showing:
- Actual vs Forecast trends  
- Demand patterns  
- Region-wise demand  

---

## Automation
A scheduler script is used to:
- Run predictions automatically at regular intervals  
- Update forecast output  
- Log execution time and status  

---

## Monitoring & Retraining
Model performance is monitored using RMSE:
- RMSE is calculated after predictions  
- If error increases, retraining can be triggered  
- New model replaces old model only if performance improves  

---

## Final Output
- Cleaned dataset : `azure_cleaned_dataset.csv`  
- Feature dataset : `feature_eng_dataset.csv`  
- Forecast output : `forecast_output.csv`  
- Model file : `model.pkl`  

---

## Conclusion
This project builds a complete pipeline from data preprocessing to prediction, deployment, and monitoring. It helps in understanding demand patterns and supports better infrastructure capacity planning.
