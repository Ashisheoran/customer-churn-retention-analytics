# Customer Churn Prediction & Retention Analytics System

## Overview

Customer churn is one of the most critical challenges faced by businesses. Acquiring a new customer is often more expensive than retaining an existing one. This project leverages Machine Learning to predict customer churn, identify high-risk customers, and provide actionable retention recommendations.

The solution includes data preprocessing, exploratory data analysis, predictive modeling using XGBoost, model evaluation, and an interactive Streamlit web application for real-time churn prediction.

---

## Problem Statement

Businesses lose significant revenue when customers discontinue their services. The objective of this project is to develop a machine learning system that can:

* Predict whether a customer is likely to churn.
* Estimate churn probability.
* Categorize customers into risk levels.
* Support customer retention strategies through predictive analytics.

---

## Dataset

The project uses an E-Commerce Customer Churn dataset containing customer demographics, engagement metrics, transaction history, and satisfaction indicators.

### Key Features

* Tenure
* City Tier
* Warehouse to Home Distance
* Hours Spent on App
* Number of Devices Registered
* Satisfaction Score
* Order Count
* Cashback Amount
* Coupon Usage
* Complaint History
* Days Since Last Order
* Marital Status
* Gender

Target Variable:

* Churn (0 = No Churn, 1 = Churn)

---

## Project Workflow

### 1. Data Preprocessing

* Missing value handling
* Feature encoding
* Data transformation
* Feature selection

### 2. Exploratory Data Analysis (EDA)

* Customer behavior analysis
* Churn distribution analysis
* Feature correlation analysis
* Business insight generation

### 3. Model Development

Algorithms evaluated:

* Logistic Regression
* K-Nearest Neighbors
* Random Forest
* AdaBoost
* Gradient Boosting
* XGBoost

### 4. Class Imbalance Handling

* SMOTE (Synthetic Minority Oversampling Technique)

### 5. Model Evaluation

Evaluation metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* Classification Report
* Confusion Matrix

---

## Final Model

**Algorithm:** XGBoost Classifier

### Performance

* Accuracy: 98.40%

XGBoost achieved the best performance among all evaluated models and was selected as the final production model.

---

## Streamlit Application

Features:

* Customer information input form
* Real-time churn prediction
* Churn probability score
* Risk categorization
* Retention recommendations

### Risk Categories

* Low Risk (< 30%)
* Medium Risk (30% – 70%)
* High Risk (> 70%)

---

## Business Insights

Key observations:

* Customers with low satisfaction scores are more likely to churn.
* Complaint history strongly influences churn behavior.
* Customers with fewer orders exhibit higher churn risk.
* Longer inactivity periods increase the likelihood of churn.
* Cashback and promotional incentives can improve retention.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Imbalanced-Learn (SMOTE)
* Joblib
* Streamlit
* Matplotlib
* Seaborn

---

## Project Structure

```text
customer-churn-prediction/

├── data/
│   └── E_Commerce_Dataset.xlsx
├── models/
│   └── churn_prediction_model.pkl
├── app/
│   └── app.py
├── churn_prediction.ipynb
├── README.md
```

---

## Results

The developed model successfully identifies customers at risk of churn with high predictive performance and provides actionable retention insights through an intuitive Streamlit application.

---

## Future Improvements

* Hyperparameter optimization
* SHAP Explainability
* Customer segmentation using clustering
* Retention recommendation engine
* Cloud deployment
* Automated model monitoring

---

## Author

Ashish

Data Science | Machine Learning | AI Enthusiast
