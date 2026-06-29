# 🛒 Customer Purchase Prediction and Recommendation System

## 📌 Project Overview

The Customer Purchase Prediction and Recommendation System is a Machine Learning-based application developed to predict whether a customer is likely to purchase a product based on their shopping behavior and engagement.

The system analyzes customer information such as product category, price, quantity, discounts, pages viewed, time spent on the website, and cart activity. Based on these inputs, the model predicts purchasing behavior and provides recommendations to improve customer engagement and sales.

---

## 🎯 Problem Statement

E-commerce businesses often struggle to identify customers who are likely to purchase products. As a result, marketing efforts may be directed toward the wrong audience, leading to reduced sales and inefficient use of resources.

This project aims to develop a predictive system that can identify potential buyers and provide personalized recommendations based on customer behavior.

---

## 💡 Proposed Solution

A Machine Learning model is trained using customer shopping behavior data. The model predicts whether a customer is likely to make a purchase and provides intelligent recommendations based on the prediction result.

---

## 🗂 Dataset Information

Dataset Name: **Ecommerce_New.csv**

Number of Records: **25,000**

Number of Features: **8**

### Features Used

| Feature | Description |
|----------|-------------|
| Product Category | Type of Product |
| Unit Price | Price of Product |
| Quantity | Quantity Selected |
| Discount(%) | Discount Offered |
| Pages Viewed | Number of Pages Visited |
| Time on Site (Sec) | Time Spent on Website |
| Added to Cart | Cart Status |
| Purchased | Target Variable |

---

## ⚙️ Technologies Used

- Python
- Pandas
- Scikit-Learn
- Joblib
- Streamlit

---

## 🧠 Machine Learning Model

The project uses the **Random Forest Classifier** algorithm for classification.

### Model Workflow

1. Data Loading
2. Data Preprocessing
3. Label Encoding
4. Train-Test Split
5. Model Training
6. Model Evaluation
7. Prediction Generation

### Model Accuracy

**74.96%**

---

## 📁 Project Structure

```text
Customer-Purchase-Prediction/
│
├── Ecommerce_New.csv
├── train_model.py
├── app.py
├── purchase_model.pkl
├── category_encoder.pkl
├── README.md
└── requirements.txt
