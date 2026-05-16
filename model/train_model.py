import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# LOAD DATA
df = pd.read_csv("data/processed_sales.csv")

# FEATURES & TARGET
# We convert product & region into numbers (simple encoding)
df["product"] = df["product"].astype("category").cat.codes
df["region"] = df["region"].astype("category").cat.codes

X = df[["product", "region", "sales", "price"]]
y = df["total_sales"]

# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# MODEL
model = LinearRegression()
model.fit(X_train, y_train)

# ACCURACY
score = model.score(X_test, y_test)
print("Model Accuracy:", score)

# SAVE MODEL
with open("model/sales_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")