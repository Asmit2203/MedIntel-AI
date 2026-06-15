import os
import shap
import joblib
import pandas as pd

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

model = None


def get_model():

    global model

    if model is None:

        print("Loading SHAP Model...")

        model = joblib.load(
            MODEL_PATH
        )

    return model


def explain_prediction(
    feature_vector,
    feature_names
):

    model = get_model()

    explainer = shap.TreeExplainer(
        model
    )

    df = pd.DataFrame(
        [feature_vector],
        columns=feature_names
    )

    shap_values = explainer.shap_values(
        df
    )

    contributions = {}

    for feature, value in zip(
        feature_names,
        shap_values[0]
    ):

        contributions[
            feature
        ] = round(
            float(value),
            4
        )

    return contributions
