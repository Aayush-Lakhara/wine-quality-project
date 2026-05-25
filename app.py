from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler

model = joblib.load("models/wine_model.pkl")

scaler = joblib.load("models/scaler.pkl")

# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():

    return render_template("index.html")

# =========================
# PREDICTION
# =========================

@app.route("/predict", methods=["POST"])
def predict():

    features = [

        float(request.form["fixed_acidity"]),
        float(request.form["volatile_acidity"]),
        float(request.form["citric_acid"]),
        float(request.form["residual_sugar"]),
        float(request.form["chlorides"]),
        float(request.form["free_sulfur_dioxide"]),
        float(request.form["total_sulfur_dioxide"]),
        float(request.form["density"]),
        float(request.form["ph"]),
        float(request.form["sulphates"]),
        float(request.form["alcohol"])

    ]

    final_features = np.array(features).reshape(1, -1)

    scaled_data = scaler.transform(final_features)

    prediction = model.predict(scaled_data)[0]

    probability = model.predict_proba(scaled_data)[0]

    confidence = round(max(probability) * 100, 2)

    # Final Result

    if prediction == 1:

        result = "Good Wine 🍷"

        quality_score = "7 - 10"

    else:

        result = "Bad Wine ❌"

        quality_score = "3 - 6"

    return render_template(

        "index.html",

        prediction_text=f"""

        {result}

        Estimated Quality Score: {quality_score}

        Confidence: {confidence}%

        """

    )

# =========================
# RUN APP
# =========================

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)