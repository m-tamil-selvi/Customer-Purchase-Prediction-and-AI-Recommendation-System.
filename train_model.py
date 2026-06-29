import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv("Ecommerce_New.csv")

print("Dataset Loaded Successfully")
print(data.shape)

# Encode Product Category
encoder = LabelEncoder()
data["Product Category"] = encoder.fit_transform(data["Product Category"])

# Features
X = data[
    [
        "Product Category",
        "Unit Price",
        "Quantity",
        "Discount(%)",
        "Pages Viewed",
        "Time on Site (Sec)",
        "Added to Cart"
    ]
]

# Target
y = data["Purchased"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Save Model
joblib.dump(model, "purchase_model.pkl")
joblib.dump(encoder, "category_encoder.pkl")

print("Model Saved Successfully")