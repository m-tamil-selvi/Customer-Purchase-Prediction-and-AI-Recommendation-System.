import streamlit as st
import pandas as pd
import joblib

# Load Model and Encoder
model = joblib.load("purchase_model.pkl")
encoder = joblib.load("category_encoder.pkl")

# Page Settings
st.set_page_config(
    page_title="AI Purchase Prediction System",
    page_icon="🛒",
    layout="centered"
)

# Title
st.title("🛒 Customer Purchase Prediction and AI Recommendation System")

st.write(
    "Predict whether a customer is likely to purchase a product and receive AI recommendations."
)

# Product Categories
categories = [
    "Electronics",
    "Fashion",
    "Books",
    "Home & Kitchen",
    "Sports",
    "Beauty",
    "Toys",
    "Groceries"
]

# User Inputs
product_category = st.selectbox(
    "📦 Product Category",
    categories
)

unit_price = st.number_input(
    "💰 Unit Price",
    min_value=0.0,
    value=800.0
)

quantity = st.number_input(
    "🛍 Quantity",
    min_value=1,
    value=2
)

discount = st.slider(
    "🏷 Discount (%)",
    0,
    100,
    10
)

pages_viewed = st.number_input(
    "📄 Pages Viewed",
    min_value=1,
    value=15
)

time_on_site = st.number_input(
    "⏱ Time on Site (Seconds)",
    min_value=1,
    value=1000
)

added_to_cart = st.selectbox(
    "🛒 Added To Cart",
    ["No", "Yes"]
)

# Predict Button
if st.button("🔍 Predict Purchase"):

    category_encoded = encoder.transform(
        [product_category]
    )[0]

    cart_value = 1 if added_to_cart == "Yes" else 0

    sample = pd.DataFrame([[
        category_encoded,
        unit_price,
        quantity,
        discount,
        pages_viewed,
        time_on_site,
        cart_value
    ]], columns=[
        "Product Category",
        "Unit Price",
        "Quantity",
        "Discount(%)",
        "Pages Viewed",
        "Time on Site (Sec)",
        "Added to Cart"
    ])

    # Prediction Probability
    probability = model.predict_proba(sample)[0][1]

    st.divider()

    st.subheader("📊 Prediction Result")

    st.metric(
        "Purchase Probability",
        f"{probability:.1%}"
    )

    # 20% Threshold
    if probability >= 0.20:

        st.success("✅ Customer is Likely to Purchase")

        st.subheader("AI Recommendations")

        st.write("✅ Recommend similar products")
        st.write("✅ Offer bundle discounts")
        st.write("✅ Show premium products")
        st.write("✅ Prioritize customer for marketing")

    else:

        st.error("❌ Customer is Not Likely to Purchase")

        st.subheader("🤖 AI Recommendations")

        st.write("✅ Offer coupon code")
        st.write("✅ Recommend best-selling products")
        st.write("✅ Provide limited-time discounts")
        st.write("✅ Send promotional notifications")

    # Customer Insights
    st.subheader("📈 Customer Insights")

    st.write(f"📦 Category: {product_category}")
    st.write(f"💰 Unit Price: ₹{unit_price}")
    st.write(f"🛍 Quantity: {quantity}")
    st.write(f"🏷 Discount: {discount}%")
    st.write(f"📄 Pages Viewed: {pages_viewed}")
    st.write(f"⏱ Time on Site: {time_on_site} sec")

    if cart_value == 1:
        st.write("🛒 Customer added product to cart")
    else:
        st.write("🛒 Customer has not added product to cart")