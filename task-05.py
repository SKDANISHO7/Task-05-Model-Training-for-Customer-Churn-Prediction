# ==========================================================
# Task 05 - Model Training
# Machine Learning Internship - Saiket Systems
# ==========================================================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

print("=" * 60)
print("TASK 05 - MODEL TRAINING")
print("=" * 60)

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

try:
    df = pd.read_csv("Clean_Telco_Customer_Churn.csv")
    print("\nDataset Loaded Successfully!")
except FileNotFoundError:
    print("\nError: Clean_Telco_Customer_Churn.csv not found.")
    print("Please complete Task 01 first.")
    exit()

# ----------------------------------------------------------
# Separate Features and Target
# ----------------------------------------------------------

X = df.drop("Churn", axis=1)
y = df["Churn"]

print("\nDataset Shape :", df.shape)
print("Features :", X.shape[1])
print("Records :", X.shape[0])

# ----------------------------------------------------------
# Train-Test Split
# ----------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nData Split Completed Successfully!")

print("Training Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ----------------------------------------------------------
# Train Selected Model
# ----------------------------------------------------------

print("\nTraining Gradient Boosting Model...")

model = GradientBoostingClassifier(random_state=42)

model.fit(X_train, y_train)

print("Model Training Completed!")

# ----------------------------------------------------------
# Evaluate Model
# ----------------------------------------------------------

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print(f"\nModel Accuracy : {accuracy:.4f}")

# ----------------------------------------------------------
# Save Trained Model
# ----------------------------------------------------------

joblib.dump(model, "Trained_Model.pkl")

print("\nTrained model saved successfully.")

print("File Created : Trained_Model.pkl")

print("\nTASK 05 COMPLETED SUCCESSFULLY")