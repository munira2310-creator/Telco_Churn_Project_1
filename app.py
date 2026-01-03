import streamlit as st
import pandas as pd
import joblib

# Title
st.title("Telco Customer Churn Prediction")

# Load model and columns (PATHS UPDATED BELOW)
model = joblib.load("churn_model_final.pkl")
model_columns = joblib.load("model_columns.pkl")

# User inputs
# ... rest of your code ...
