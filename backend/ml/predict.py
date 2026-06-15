import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MODEL_PATH = os.path.abspath(
    os.path.join(
        BASE_DIR,
        "..",
        "..",
        "models",
        "risk_model.pkl"
    )
)

SCALER_PATH = os.path.abspath(
    os.path.join(
        BASE_DIR,
        "..",
        "..",
        "models",
        "scaler.pkl"
    )
)

print("MODEL PATH:", MODEL_PATH)
print("SCALER PATH:", SCALER_PATH)

model = None
scaler = None


def load_artifacts():

    global model
    global scaler

    if model is None:

        print("Loading Risk Model...")

        model = joblib.load(
            MODEL_PATH
        )

    if scaler is None:

        print("Loading Scaler...")

        scaler = joblib.load(
            SCALER_PATH
        )


def predict_risk(features):

    load_artifacts()

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