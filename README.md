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

