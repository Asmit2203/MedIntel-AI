import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "..",
    "Models",
    "risk_model.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "..",
    "..",
    "Models",
    "scaler.pkl"
)

model = joblib.load(
    MODEL_PATH
)

scaler = joblib.load(
    SCALER_PATH
)


def predict_risk(features):

    feature_array = np.array(
        [features]
    )

    scaled_features = scaler.transform(
        feature_array
    )

    prediction = model.predict(
        scaled_features
    )[0]

    probability = model.predict_proba(
        scaled_features
    )[0][1]

    risk_score = round(
    float(probability) * 100,
    2
)

    if risk_score < 30:
        risk_level = "Low"

    elif risk_score < 70:
        risk_level = "Moderate"

    else:
        risk_level = "High"

    return {
        "prediction": int(prediction),
        "risk_score": risk_score,
        "risk_level": risk_level
    }