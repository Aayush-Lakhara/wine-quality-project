import joblib
import numpy as np

# =========================
# LOAD SAVED MODEL
# =========================

model = joblib.load("models/wine_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# =========================
# USER INPUT
# =========================

fixed_acidity = float(input("Fixed Acidity: "))
volatile_acidity = float(input("Volatile Acidity: "))
citric_acid = float(input("Citric Acid: "))
residual_sugar = float(input("Residual Sugar: "))
chlorides = float(input("Chlorides: "))
free_sulfur_dioxide = float(input("Free Sulfur Dioxide: "))
total_sulfur_dioxide = float(input("Total Sulfur Dioxide: "))
density = float(input("Density: "))
pH = float(input("pH: "))
sulphates = float(input("Sulphates: "))
alcohol = float(input("Alcohol: "))

# =========================
# CREATE ARRAY
# =========================

data = np.array([[
    fixed_acidity,
    volatile_acidity,
    citric_acid,
    residual_sugar,
    chlorides,
    free_sulfur_dioxide,
    total_sulfur_dioxide,
    density,
    pH,
    sulphates,
    alcohol
]])

# =========================
# SCALE DATA
# =========================

data_scaled = scaler.transform(data)

# =========================
# PREDICTION
# =========================

prediction = model.predict(data_scaled)

print("\nPredicted Wine Quality:", prediction[0])