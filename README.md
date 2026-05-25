# 🍷 Wine Quality Classification

This is a Machine Learning project that predicts wine quality using physicochemical features such as acidity, alcohol level, sugar content, pH, and more.

The model classifies wine into:

- Low Quality
- Medium Quality
- High Quality

---

# 🚀 Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Joblib

---

# 📂 Project Structure

```text
wine_quality_project/
│
├── data/
│   └── winequality.csv
│
├── models/
│   ├── wine_model.pkl
│   └── scaler.pkl
│
├── train_model.py
├── predict.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Features

- Multi-class classification
- Feature scaling using StandardScaler
- Random Forest Classifier
- Model saving with Joblib
- Prediction system without retraining

---

# 📊 Dataset

Dataset Source:
UCI Machine Learning Repository

Dataset used:
- winequality-red.csv

---

# ▶️ How To Run

## 1️⃣ Install Libraries

```bash
pip install -r requirements.txt
```

---

## 2️⃣ Train Model

```bash
python train_model.py
```

This will:
- train the model
- save model files inside `models/`

---

## 3️⃣ Predict Wine Quality

```bash
python predict.py
```

Enter input values and the model will predict wine quality.

---

# 🧠 Machine Learning Concepts Used

- Classification
- Random Forest
- Feature Scaling
- Train-Test Split
- Model Evaluation
- Accuracy Score

---

# 📌 Future Improvements

- GUI using Tkinter
- Flask Web App
- Hyperparameter Tuning
- ROC-AUC Curve
- Streamlit Deployment

---

# 👨‍💻 Author

Aayush Lakhara