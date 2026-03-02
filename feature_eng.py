import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\gorak\\OneDrive\\Desktop\\azure\\datasets\\azure_cleaned_dataset.csv")

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], dayfirst=True)

# Sort by time
df = df.sort_values('timestamp')

print("Initial Shape:", df.shape)



# 2. Time-based Features 

df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.dayofweek
df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)

print("Time features added.")


# 3. Lag Features

df['target_lag_1'] = df['target'].shift(1)      # previous hour
df['target_lag_24'] = df['target'].shift(24)    # previous day

print("Lag features added.")



#rolling mean
df['rolling_mean'] = df['target'].rolling(24).mean()

print("Rolling feature added.")


threshold = df['target'].mean() + 2 * df['target'].std()
df['spike_flag'] = (df['target'] > threshold).astype(int)

print("Spike feature added.")



df = pd.get_dummies(df, columns=['region', 'vm_type', 'cloud_provider'], drop_first=True)
print("Categorical encoding done.")



df = df.dropna()
print("Final Shape:", df.shape)


df.to_csv("feature_eng_dataset.csv", index=False)
print("Feature Engineering Completed Successfully.")