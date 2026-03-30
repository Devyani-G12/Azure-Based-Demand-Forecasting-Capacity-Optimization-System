## Azure-Based Demand Forecasting & Capacity Optimization System
About the Project

This project is about analyzing Azure usage data and predicting future demand. The main goal is to understand how resources are used and estimate future needs so that capacity can be managed better.

## Dataset

The dataset includes:

Timestamp
Region
CPU usage
Memory usage
Disk and network activity
VM configuration
Cost and utilization
External factors like GDP and electricity price
Data Cleaning

The dataset was cleaned by handling missing values and removing unnecessary data. Some columns were also formatted properly for easier analysis.

## Feature Engineering

New features were created like day, month, and usage trends from timestamp data. This helped in improving the prediction.

## Model Used

In this project, simple machine learning models like Linear Regression and time-series methods were used. The model was trained on past usage data to predict future demand.

## Model Evaluation

The model performance was checked using basic metrics like:

Mean Absolute Error (MAE)
Mean Squared Error (MSE)

These metrics helped to understand how accurate the predictions are.

## Results

The model was able to predict future resource usage with reasonable accuracy. It showed trends of increasing or decreasing demand over time. This can help in planning resources in advance and reducing wastage.

## Conclusion

This project shows how machine learning can be useful in cloud capacity planning. With better models and more data, the predictions can be improved further.
