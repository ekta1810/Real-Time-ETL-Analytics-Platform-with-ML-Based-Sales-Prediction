import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

st.title("📊 Real-Time ETL Analytics Platform")

# LOAD DATA
df = pd.read_csv("data/processed_sales.csv")
st.subheader("📁 Dataset Preview")
st.dataframe(df)

# INPUT SECTION
st.subheader("🔮 Make Prediction")

product = st.number_input("Product (numeric)", value=0)
region = st.number_input("Region (numeric)", value=0)
sales = st.number_input("Sales", value=0)
price = st.number_input("Price", value=0)

# BUTTON
if st.button("Predict"):
    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json={
                "product": product,
                "region": region,
                "sales": sales,
                "price": price
            }
        )

        result = response.json()
        st.success(f"Predicted Sales: {result['predicted_sales']}")

       
        # 📊 CHART SECTION (ADD HERE)
       

        df_chart = df.copy()

       
        df_chart["product"] = df_chart["product"].astype("category").cat.codes
        df_chart["region"] = df_chart["region"].astype("category").cat.codes

        predictions = []

        for i in range(len(df_chart)):
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json={
                    "product": int(df_chart.iloc[i]["product"]),
                    "region": int(df_chart.iloc[i]["region"]),
                    "sales": float(df_chart.iloc[i]["sales"]),
                    "price": float(df_chart.iloc[i]["price"])
                }
            )
            predictions.append(response.json()["predicted_sales"])

        df_chart["predicted_sales"] = predictions

        # PLOT
        fig, ax = plt.subplots()

        ax.plot(df_chart["sales"].values, label="Actual Sales", marker="o")
        ax.plot(df_chart["predicted_sales"].values, label="Predicted Sales", marker="x")

        ax.set_title("Actual vs Predicted Sales")
        ax.set_xlabel("Data Points")
        ax.set_ylabel("Sales")
        ax.legend()

        st.pyplot(fig)

    except Exception as e:
        st.error(f"API Error: {e}")
