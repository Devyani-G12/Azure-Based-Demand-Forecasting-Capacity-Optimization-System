import numpy as np
import pandas as pd

df= pd.read_csv("azure_project_dataset.csv")

df['timestamp'] = pd.to_datetime(df['timestamp']) # timestamp -> timeseries
df = df.sort_values('timestamp')


print("\nMissing values before cleaning:")
print(df.isnull().sum())

# numeric value (missing) handling
n_cols = df.select_dtypes(include=np.number).columns

df[n_cols] = df[n_cols].interpolate()
df[n_cols] = df[n_cols].fillna(df[n_cols].median())


# categorical value 
cate_cols = df.select_dtypes(include='object').columns

for col in cate_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# mapping region with cloud region
df['region'] = df['region'].str.strip()
region_map = {
    "East US": "us-east",
    "West Europe": "europe-west",
    "Central India": "asia-south",
    "Japan East": "asia-east",
    "Southeast Asia": "asia-southeast"
}

df['region'] = df['region'].replace(region_map)

df = df.drop_duplicates() # removing duplicates 

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nFinal dataset shape:", df.shape)

df.to_csv("azure_cleaned_dataset.csv", index=False)
print("\nCleaned dataset saved successfully.")
