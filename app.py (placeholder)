import streamlit as st
import pandas as pd
import joblib

# Title
st.title("Telco Customer Churn Prediction")

# Load model and columns
model = joblib.load("TELCO_1/churn_model_final.pkl")
model_columns = joblib.load("TELCO_1/model_columns.pkl")

# User inputs
st.sidebar.header("Customer Details")

input_data = {}
for col in model_columns:
    input_data[col] = st.sidebar.number_input(f"{col}", min_value=0.0)

input_df = pd.DataFrame([input_data])

# Predict
if st.button("Predict Churn"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    st.write(f"Predicted Churn: {'Yes' if prediction==1 else 'No'}")
    st.write(f"Churn Probability: {probability*100:.2f}%")
