import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("data/winequality.csv", sep=";")

print(df.head())

# =========================
# CREATE CLASSES
# =========================

def quality_label(q):
    if q <= 4:
        return "Low"
    elif q <= 6:
        return "Medium"
    else:
        return "High"

df["quality_label"] = df["quality"].apply(quality_label)

# =========================
# FEATURES AND TARGET
# =========================

X = df.drop(["quality", "quality_label"], axis=1)
y = df["quality_label"]

# =========================
# FEATURE SCALING
# =========================

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# MODEL TRAINING
# =========================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# =========================
# PREDICTION
# =========================

y_pred = model.predict(X_test)

# =========================
# EVALUATION
# =========================

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# =========================
# SAVE MODEL
# =========================

joblib.dump(model, "models/wine_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("\nModel saved successfully!")