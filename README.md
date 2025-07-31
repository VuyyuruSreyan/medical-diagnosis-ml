# 🩺 Medical Diagnosis Using Machine Learning

A machine learning-based web application that predicts the presence of heart disease using medical features.

---

## 🚀 Overview

This project demonstrates how machine learning can assist in early diagnosis of cardiovascular conditions. The app predicts whether a patient is likely to have heart disease based on input features.

> ⚡ Designed for real-world impact — ideal for healthcare applications and internship portfolios.

---

## 🛠️ Tech Stack

- **Python** – Data handling and ML model
- **Scikit-Learn** – Model training and evaluation
- **Flask** – Web application backend
- **HTML/CSS** – Minimal frontend
- **Joblib** – Model serialization

---

## 📊 Dataset

The dataset used is the **Heart Disease UCI dataset**, which contains patient data and diagnosis outcomes.

- [🔗 UCI Dataset Link](https://www.kaggle.com/datasets/ronitf/heart-disease-uci)

heart.csv
├── age
├── sex
├── cp
├── trestbps
├── chol
├── fbs
├── restecg
├── thalach
├── exang
├── oldpeak
├── slope
├── ca
├── thal
└── target (0 = No Disease, 1 = Disease)

yaml
Copy
Edit

---

## 📦 Project Structure

MedicalDiagnosis/
├── model/
│ └── diagnosis_model.pkl ← Trained ML model
├── templates/
│ └── index.html ← Input form UI
├── app.py ← Flask application
├── train_model.py ← Model training script
├── requirements.txt ← Dependencies
└── README.md ← This file

yaml
Copy
Edit

---

## 🧠 How It Works

1. User inputs values for 11 medical features (e.g., age, BP, cholesterol)
2. The trained Random Forest model predicts diagnosis
3. Result is displayed: **Positive** or **Negative** (Heart Disease)

---

## ⚙️ Running Locally

### 🔧 Install Dependencies
```bash
pip install -r requirements.txt
🧪 Train the Model
bash
Copy
Edit
python train_model.py
🚀 Start the App
bash
Copy
Edit
python app.py
Go to http://localhost:5000 in your browser.

📈 Results
Model Used: Random Forest Classifier

Accuracy Achieved: ~73%

Focused on improving recall to minimize false negatives in medical diagnosis.

💼 Internship Ready
This project reflects:

Real-world dataset usage

Full ML pipeline from training to deployment

Production-ready model with a clean UI

Clear application in healthcare, ideal for resume & paid internship showcases

📬 Contact
Feel free to connect or reach out:

📧 Email: vuyyurusreyan@gmail.com

🔗 LinkedIn: linkedin.com/in/vuyyurusreyan

yaml
Copy
Edit

---

### ✅ Next Step:
Save this as `README.md` inside your `MedicalDiagnosis/` folder.

Once done, push it to GitHub using:

```bash
git add README.md
git commit -m "📝 Added professional README for internship showcase"
git push
