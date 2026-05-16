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
sales = st.number_input("Sales", value=0.0)
price = st.number_input("Price", value=0.0)

API_URL = "https://real-time-etl-analytics-platform-with-ml.onrender.com/predict"


# PREDICTION BUTTON

if st.button("Predict"):
    try:
        response = requests.post(
            API_URL,
            json={
                "product": product,
                "region": region,
                "sales": sales,
                "price": price
            },
            timeout=10
        )

        if response.status_code != 200:
            st.error(f"Server Error: {response.text}")
            st.stop()

        result = response.json()

        st.write("API Response:", result)  # DEBUG (important)

        prediction = result.get("predicted_sales")

        if prediction is None:
            st.error("Invalid API response: 'predicted_sales' not found")
            st.stop()

        st.success(f"Predicted Sales: {prediction}")

        
        # CHART SECTION
       
        st.subheader("📊 Actual vs Predicted Sales")

        df_chart = df.copy()

        # encode categorical values safely
        df_chart["product"] = df_chart["product"].astype("category").cat.codes
        df_chart["region"] = df_chart["region"].astype("category").cat.codes

        predictions = []

        # LIMIT LOOP (avoid API overload)
        for i in range(min(20, len(df_chart))):
            try:
                r = requests.post(
                    API_URL,
                    json={
                        "product": int(df_chart.iloc[i]["product"]),
                        "region": int(df_chart.iloc[i]["region"]),
                        "sales": float(df_chart.iloc[i]["sales"]),
                        "price": float(df_chart.iloc[i]["price"])
                    },
                    timeout=10
                )

                if r.status_code == 200:
                    predictions.append(r.json().get("predicted_sales", 0))
                else:
                    predictions.append(0)

            except:
                predictions.append(0)

        df_chart = df_chart.head(len(predictions))
        df_chart["predicted_sales"] = predictions

        
        # PLOT
        
        fig, ax = plt.subplots()

        ax.plot(df_chart["sales"].values, label="Actual Sales")
        ax.plot(df_chart["predicted_sales"].values, label="Predicted Sales")

        ax.set_title("Actual vs Predicted Sales")
        ax.set_xlabel("Data Points")
        ax.set_ylabel("Sales")
        ax.legend()

        st.pyplot(fig)

    except Exception as e:
        st.error(f"API Error: {e}")
