import joblib
import pandas as pd
import os

# Get the folder path where predict.py exists
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load models
reg_model = joblib.load(os.path.join(BASE_DIR, "best_regression_model.pkl"))
clf_model = joblib.load(os.path.join(BASE_DIR, "best_classification_model.pkl"))

# Load scalers
scaler_r = joblib.load(os.path.join(BASE_DIR, "scaler_regression.pkl"))
scaler_c = joblib.load(os.path.join(BASE_DIR, "scaler_classification.pkl"))

# Load label encoder
label_enc = joblib.load(os.path.join(BASE_DIR, "label_encoder.pkl"))

def predict_air_quality(pm25, pm10, no2, so2, co, o3):
    new_data = pd.DataFrame([{
        "PM2.5": pm25,
        "PM10": pm10,
        "NO2": no2,
        "SO2": so2,
        "CO": co,
        "O3": o3
    }])

    scaled_r = scaler_r.transform(new_data)
    scaled_c = scaler_c.transform(new_data)

    pred_aqi = reg_model.predict(scaled_r)[0]
    pred_cat_encoded = clf_model.predict(scaled_c)[0]

    pred_cat = label_enc.inverse_transform([pred_cat_encoded])[0]

    risk_map = {
        "Good": "Air quality is satisfactory. No health risk.",
        "Satisfactory": "Air quality is acceptable.",
        "Moderate": "Sensitive groups should limit outdoor activity.",
        "Poor": "Breathing discomfort possible.",
        "Very Poor": "Health effects may be experienced.",
        "Severe": "Avoid outdoor activity."
    }

    health_msg = risk_map.get(pred_cat, "Unknown")

    return pred_aqi, pred_cat, health_msg
