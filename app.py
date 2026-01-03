# app.py - Streamlit deploy-ready

import streamlit as st
import pandas as pd
import joblib
import os

# -------------------------------
# Base directory (repo-relative)
BASE_DIR = os.path.dirname(__file__)

# Paths to model & columns
MODEL_PATH = os.path.join(BASE_DIR, "model", "churn_model_final.pkl")
COLUMNS_PATH = os.path.join(BASE_DIR, "model", "model_columns.pkl")

# -------------------------------
# Load model & columns
try:
    model = joblib.load(MODEL_PATH)
    model_columns = joblib.load(COLUMNS_PATH)
except FileNotFoundError:
    st.error("Model files not found! Make sure churn_model_final.pkl and model_columns.pkl are in the 'model/' folder.")
    st.stop()

# -------------------------------
# App title
st.title("📊 Telco Customer Churn Prediction")

st.write("""
Predict whether a telecom customer is likely to churn.
Fill in the customer details below and click **Predict Churn**.
""")

# -------------------------------
# Sidebar inputs
st.sidebar.header("Customer Details Input")

input_data = {}
for col in model_columns:
    # assuming all features are numeric for simplicity
    input_data[col] = st.sidebar.number_input(f"{col}", min_value=0.0, value=0.0)

input_df = pd.DataFrame([input_data])

# -------------------------------
# Prediction
if st.button("Predict Churn"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result:")
    st.write(f"Predicted Churn: **{'Yes' if prediction==1 else 'No'}**")
    st.write(f"Churn Probability: **{probability*100:.2f}%**")
