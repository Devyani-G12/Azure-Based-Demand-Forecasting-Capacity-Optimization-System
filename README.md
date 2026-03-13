# Azure-Based-Demand-Forecasting-Capacity-Optimization-System
About the Project 
The project focuses on preparing Azure infrastructure usage data for time-series analysis and demand forecasting.

Dataset :
The project uses a dataset that contains Azure infrastructure usage information such as :
- timestamp
- region
- cpu_usage
- memory_usage
- disk_and_network_activity
- VM configuration
- cost and utilization
- external variables like GDP growth and electricity price
  
  
Data Cleaning Steps :

The preprocessing script performs the following steps:
1.Loads the raw dataset
2.Converts timestamp into datetime format
3.Sorts data for time-series analysis
4.Handles missing numeric values using interpolation and median
5.Handles missing categorical values using mode
6.Standardizes region names into cloud region codes
7.Removes duplicate records
8.Saves the cleaned dataset

Output :
After preprocessing, a cleaned dataset is generated:
azure_cleaned_dataset.csv

Feature Engineering :

After cleaning the dataset, additional features were created to help the models capture usage patterns.

- Time-based features such as hour, day_of_week, and is_weekend were extracted from the timestamp.
- Lag features (target_lag_1 and target_lag_24) were created to represent previous demand values.
- A rolling_mean feature was calculated over 24 hours to capture short-term demand trends.
- A spike_flag feature was created to identify sudden spikes in demand.
- Categorical columns like region, vm_type, and cloud_provider were converted to numeric form using one-hot encoding.
- Rows with missing values created during lag and rolling calculations were removed.


Output :
The processed dataset used for model training was saved as:
feature_eng_dataset.csv


Model Training :
Two forecasting models were implemented:
- ARIMA – a time-series model that predicts demand using historical target values.
- XGBoost – a machine learning model that uses engineered features to predict demand.
The dataset was split into training and testing sets while maintaining the time order of the data.

Models were evaluated using the following metrics:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Square Error)
- Forecast Bias
Hyperparameter tuning was applied to the XGBoost model using GridSearchCV, and rolling validation was used for backtesting.


Model Comparison :
ARIMA Results
- MAE : 15.75
- RMSE : 19.97
- Bias : -12.83

XGBoost Results
- MAE : 3.95
- RMSE : 6.00
- Bias : 0.23

XGBoost showed significantly lower error values and a bias close to zero, indicating more accurate and balanced predictions. Therefore, XGBoost was selected as the final model for demand forecasting.

Final Output :
- Cleaned dataset : azure_cleaned_dataset.csv  
- Feature engineered dataset : feature_eng_dataset.csv  
- Forecasting models : ARIMA and XGBoost
