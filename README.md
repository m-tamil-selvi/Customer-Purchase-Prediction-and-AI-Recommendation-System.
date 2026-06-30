# 🛒 Customer Purchase Prediction and Recommendation System

## 📖 Project Overview

The Customer Purchase Prediction and Recommendation System is a Machine Learning-based application developed to predict whether a customer is likely to purchase a product based on their shopping behavior and engagement.

The system analyzes customer activities such as product category selection, product price, quantity, discounts, pages viewed, time spent on the website, and cart activity. Based on these inputs, the trained machine learning model predicts customer purchase behavior and provides personalized recommendations.

This project demonstrates the practical application of Machine Learning in the E-commerce domain to support data-driven business decisions and improve customer engagement.

---

# 🎯 Problem Statement

E-commerce businesses generate large amounts of customer interaction data every day. However, identifying customers who are likely to make a purchase remains a challenge.

Without proper analysis:

- Marketing resources may be wasted on uninterested customers.
- Potential customers may not receive targeted offers.
- Sales opportunities may be missed.

A predictive system is required to analyze customer behavior and identify purchase intent, enabling businesses to make informed marketing and recommendation decisions.

---

# 💡 Proposed Solution

This project uses Machine Learning techniques to analyze customer shopping behavior and predict whether a customer is likely to purchase a product.

The system takes customer-related inputs such as:

- Product Category
- Unit Price
- Quantity
- Discount Percentage
- Pages Viewed
- Time Spent on Website
- Added to Cart Status

The trained model processes these inputs and predicts purchase behavior. Based on the prediction result, the system generates personalized recommendations to improve customer engagement and increase conversion rates.

---

# 📊 Dataset Information

**Dataset Name:** Ecommerce_New.csv

**Total Records:** 25,000

**Total Features:** 8

### Dataset Features

| Feature | Description |
|----------|-------------|
| Product Category | Category of Product |
| Unit Price | Product Price |
| Quantity | Quantity Selected |
| Discount(%) | Discount Offered |
| Pages Viewed | Number of Pages Visited |
| Time on Site (Sec) | Time Spent on Website |
| Added to Cart | Indicates whether the product was added to cart |
| Purchased | Target Variable |

---

# 🧹 Data Preprocessing

The dataset was cleaned and simplified to improve model performance and project usability.

The preprocessing stage included:

- Removal of unnecessary columns
- Feature selection
- Data cleaning
- Label Encoding of Product Category
- Train-Test Data Splitting

Product categories were converted into numerical values using Label Encoding because Machine Learning models cannot directly process textual data.

Example:

```text
Electronics → 0
Fashion → 1
Books → 2
Home & Kitchen → 3
Sports → 4
Beauty → 5
Toys → 6
Groceries → 7
```

---

# 🧠 Machine Learning Model

The project uses the **Random Forest Classifier** algorithm.

Random Forest is a supervised machine learning algorithm that combines multiple decision trees to improve prediction performance and reduce overfitting.

### Model Workflow

1. Load Dataset
2. Encode Product Categories
3. Split Dataset into Training and Testing Sets
4. Train Random Forest Model
5. Evaluate Model Performance
6. Save Trained Model
7. Generate Predictions

### Model Accuracy

```text
Accuracy: 74.96%
```

---

# 📚 Libraries Used

### Pandas

Used for:

- Reading CSV files
- Data manipulation
- Data preprocessing

```python
import pandas as pd
```

### Scikit-Learn

Used for:

- Label Encoding
- Train-Test Splitting
- Model Training
- Model Evaluation

```python
from sklearn.ensemble import RandomForestClassifier
```

### Joblib

Used for:

- Saving trained models
- Loading trained models

```python
import joblib
```

### Streamlit

Used for:

- Building interactive web applications
- User Interface creation
- Real-time prediction display

```python
import streamlit as st
```

---

# 💾 Saved Model Files

## purchase_model.pkl

This file contains the trained Random Forest machine learning model.

Purpose:

- Stores learned patterns from training data.
- Eliminates the need to retrain the model every time.
- Used for generating customer purchase predictions.

Created using:

```python
joblib.dump(model, "purchase_model.pkl")
```

---

## category_encoder.pkl

This file stores the Label Encoder used during preprocessing.

Purpose:

- Converts product category names into numerical values.
- Ensures consistency between training and prediction phases.

Created using:

```python
joblib.dump(encoder, "category_encoder.pkl")
```

---

# 🏗️ System Architecture

```text
User Input
     ↓
Streamlit User Interface
     ↓
Category Encoder
     ↓
Random Forest Model
     ↓
Purchase Prediction
     ↓
Recommendation Generation
```

The user enters product and customer behavior details through the Streamlit interface. The product category is encoded into numerical form and passed to the trained Random Forest model. The model predicts customer purchase behavior and generates recommendations based on the prediction result.

---

# ✨ Features

- Customer Purchase Prediction
- Purchase Probability Analysis
- Personalized Recommendations
- Interactive Streamlit Interface
- Clean and User-Friendly Design
- Machine Learning-Based Decision Making
- Real-Time Prediction Generation

---

# 📁 Project Structure

```text
Customer-Purchase-Prediction-System/
│
├── Ecommerce_New.csv
├── train_model.py
├── app.py
├── purchase_model.pkl
├── category_encoder.pkl
├── requirements.txt
└── README.md
```

---

# 🚀 How to Run the Project

## Step 1: Clone the Repository

```bash
git clone https://github.com/m-tamil-selvi/customer-purchase-prediction-and-ai-recommendation-system..git
```

## Step 2: Navigate to Project Directory

```bash
cd customer-purchase-prediction-and-ai-recommendation-system.
```

## Step 3: Install Required Libraries

```bash
pip install pandas scikit-learn streamlit joblib
```

Or use:

```bash
pip install -r requirements.txt
```

## Step 4: Train the Model

```bash
python train_model.py
```

This will generate:

```text
purchase_model.pkl
category_encoder.pkl
```

## Step 5: Run Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

# 📈 Results

The developed system successfully predicts customer purchase behavior based on shopping activity and engagement.

### Model Performance

```text
Accuracy: 74.96%
```

### Prediction Output

- Likely to Purchase
- Not Likely to Purchase

### Recommendations

- Product Suggestions
- Promotional Offers
- Discount Recommendations
- Marketing Prioritization

---

# 🔮 Future Enhancements

The project can be further improved by:

- Integrating real-time customer data
- Implementing advanced recommendation engines
- Deploying the application to cloud platforms
- Using deep learning models for improved accuracy
- Customer segmentation and personalization
- Integration with e-commerce platforms

---

# 🎓 Academic Relevance

This project demonstrates the practical application of:

- Machine Learning
- Classification Algorithms
- Data Preprocessing
- Model Deployment
- Recommendation Systems
- Streamlit Web Applications

It serves as a beginner-friendly AIML project showcasing the complete machine learning workflow from data preprocessing to deployment.

---

# 👨‍💻 Author

**M.Tamil Selvi**

Machine Learning and AI Enthusiast

Academic Project developed using Python, Scikit-Learn, and Streamlit.
