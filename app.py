import joblib
import numpy as np

# Load the model
model = joblib.load("model/diagnosis_model.pkl")

# diabetes.csv columns (Pima Indians): 
# Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
input_data = [2, 120, 70, 20, 79, 25.0, 0.5, 33]   # example values


# Convert to numpy array and reshape
input_array = np.array(input_data).reshape(1, -1)

# Make prediction
prediction = model.predict(input_array)
print("Prediction:", "Positive" if prediction[0] == 1 else "Negative")
