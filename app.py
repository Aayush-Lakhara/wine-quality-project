from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load("models/wine_model.pkl")
scaler = joblib.load("models/scaler.pkl")

@app.route("/")
def home():
    return "Wine Quality Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    features = np.array(data["features"]).reshape(1, -1)

    scaled_data = scaler.transform(features)

    prediction = model.predict(scaled_data)

    return jsonify({
        "prediction": int(prediction[0])
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)