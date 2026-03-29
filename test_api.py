import requests

url = "http://127.0.0.1:5000/predict"

data = [
    {
        "CPU": 4,
        "RAM_GB": 16,
        "price_per_hour": 0.5,
        "latency_ms": 120,
        "throughput": 300,
        "cost": 150,
        "utilization": 0.75,
        "gdp_growth": 6.5,
        "electricity_price_index": 120,
        "hour": 10,
        "day_of_week": 2,
        "is_weekend": 0,
        "target_lag_1": 120,
        "target_lag_24": 110,
        "rolling_mean": 115,
        "spike_flag": 0,
        "region_asia-south": 1,
        "region_asia-southeast": 0,
        "region_europe-west": 0,
        "region_us-east": 0,
        "vm_type_Standard_D4s_v3": 1,
        "vm_type_Standard_E8s_v4": 0,
        "vm_type_Standard_F8s_v2": 0
    }
]

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)