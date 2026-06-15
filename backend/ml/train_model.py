import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    classification_report,
)

from xgboost import XGBClassifier


# -----------------------------
# Paths
# -----------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "..",
    "..",
    "datasets",
    "diabetes.csv"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "..",
    "..",
    "models"
)

os.makedirs(
    MODEL_DIR,
    exist_ok=True
)

# -----------------------------
# Load Dataset
# -----------------------------

print(f"\nLoading dataset from:\n{DATASET_PATH}")

df = pd.read_csv(DATASET_PATH)

print("\nDataset Shape:")
print(df.shape)

# -----------------------------
# Features & Target
# -----------------------------

X = df.drop(
    columns=["Outcome"]
)

y = df["Outcome"]

# -----------------------------
# Feature Scaling
# -----------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# -----------------------------
# Train Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------------
# Model
# -----------------------------

model = XGBClassifier(
    n_estimators=150,
    max_depth=5,
    learning_rate=0.05,
    objective="binary:logistic",
    random_state=42
)

# -----------------------------
# Training
# -----------------------------

print("\nTraining model...")

model.fit(
    X_train,
    y_train
)

# -----------------------------
# Evaluation
# -----------------------------

predictions = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(
    f"\nAccuracy: {accuracy:.4f}"
)

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        predictions
    )
)

# -----------------------------
# Save Model
# -----------------------------

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "risk_model.pkl"
)

SCALER_PATH = os.path.join(
    MODEL_DIR,
    "scaler.pkl"
)

joblib.dump(
    model,
    MODEL_PATH
)

joblib.dump(
    scaler,
    SCALER_PATH
)

print("\nModel saved successfully.")

print(f"\nModel: {MODEL_PATH}")
print(f"Scaler: {SCALER_PATH}")