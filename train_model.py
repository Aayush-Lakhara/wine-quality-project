import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

from xgboost import XGBClassifier

from imblearn.over_sampling import SMOTE

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("data/winequality.csv", sep=";")

print("\nFirst 5 Rows:\n")

print(df.head())

# =========================
# CREATE BINARY TARGET
# =========================

# 0 = Bad Wine
# 1 = Good Wine

df["wine_category"] = df["quality"].apply(
    lambda x: 1 if x >= 7 else 0
)

# =========================
# CLASS DISTRIBUTION
# =========================

print("\nClass Distribution:\n")

print(df["wine_category"].value_counts())

# =========================
# FEATURES AND TARGET
# =========================

X = df.drop(["quality", "wine_category"], axis=1)

y = df["wine_category"]

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

    random_state=42,

    stratify=y

)

# =========================
# APPLY SMOTE
# =========================

print("\nApplying SMOTE...\n")

smote = SMOTE(random_state=42)

X_train, y_train = smote.fit_resample(X_train, y_train)

print("\nBalanced Class Distribution:\n")

print(pd.Series(y_train).value_counts())

# =========================
# MODEL TRAINING
# =========================

print("\nTraining XGBoost Model...\n")

model = XGBClassifier(

    n_estimators=500,

    learning_rate=0.05,

    max_depth=6,

    subsample=0.8,

    colsample_bytree=0.8,

    random_state=42,

    eval_metric='logloss'

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

print("\nModel Saved Successfully!")