from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(title="ETL ML Prediction API")

# LOAD MODEL
model = pickle.load(open("model/sales_model.pkl", "rb"))

# INPUT SCHEMA
class InputData(BaseModel):
    product: int
    region: int
    sales: float
    price: float

# HOME ROUTE
@app.get("/")
def home():
    return {"message": "ML API is running"}

# PREDICTION ROUTE
@app.post("/predict")
def predict(data: InputData):
    input_array = np.array([[
        data.product,
        data.region,
        data.sales,
        data.price
    ]])

    prediction = model.predict(input_array)

    return {
        "predicted_sales": float(prediction[0])
    }