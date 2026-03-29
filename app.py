from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("C:/Users/gorak/OneDrive/Desktop/azure/model/model.pkl")

cols = [
    "cpu_usage","memory_usage","net_io","disk_io","vCPU",
    "RAM_GB","price_per_hour","latency_ms","throughput","cost",
    "utilization","gdp_growth","electricity_price_index",
    "hour","day_of_week","is_weekend",
    "target_lag_1","target_lag_24","rolling_mean","spike_flag",
    "region_asia-south","region_asia-southeast","region_europe-west","region_us-east",
    "vm_type_Standard_D4s_v3","vm_type_Standard_E8s_v4","vm_type_Standard_F8s_v2"
]

@app.route('/')
def home():
    return "API running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame(data)

    for c in cols:
        if c not in df.columns:
            df[c] = 0

    df = df[cols]

    result = model.predict(df)

    return jsonify(result.tolist())

app.run(debug=True)