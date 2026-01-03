

### \# Telco Customer Churn Prediction



\## 📌 Project Overview

This project predicts whether a telecom customer is likely to churn using machine learning.

The goal is to help businesses proactively retain customers by identifying churn risk early.



\## 🧠 Problem Statement

Customer churn directly impacts revenue. Using historical customer data, this project builds

a classification model to predict churn and highlight key factors influencing customer decisions.



\## 📊 Dataset

\- Source: IBM Telco Customer Churn Dataset

\- Records: ~7,000 customers

\- Target Variable: `Churn` (Yes / No)



\## ⚙️ Tech Stack

\- Python

\- Pandas, NumPy

\- Scikit-learn

\- Matplotlib, Seaborn

\- Streamlit (optional for app deployment)



\## 🏗️ Model Used

\- Random Forest Classifier



\## 📈 Model Performance

| Metric        | Score |

|---------------|-------|

| Accuracy      | ~94%  |

| Precision     | High  |

| Recall        | High  |

| F1-Score      | High  |

| ROC-AUC       | Added |



> Note: Accuracy alone is not sufficient due to class imbalance. Additional metrics are used.



\## 🔍 Key Features Affecting Churn

\- Contract Type

\- Monthly Charges

\- Tenure

\- Internet Service

\- Payment Method



\## 🚀 How to Run Locally

```bash

git clone https://github.com/munira2310-creator/Telco-Customer-churn-Prediction.git

cd Telco-Customer-churn-Prediction

pip install -r requirements.txt

streamlit run app.py



