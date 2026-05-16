# Real-Time ETL Analytics Platform 🚀

## 📌 Project Overview
This project is a Real-Time ETL-based Analytics Platform that processes sales data, performs data transformation, and applies Machine Learning to predict future sales. It also includes an interactive Streamlit dashboard for visualization.

---

## ⚙️ Features
- Data ingestion (CSV-based ETL pipeline)
- Data cleaning & feature engineering
- Machine Learning model for sales prediction
- Interactive Streamlit dashboard
- Data visualization (charts + tables)

---

## 🧠 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Matplotlib

---

## 📊 Workflow
Data → ETL Pipeline → Processed Data → ML Model → Dashboard

---

## 🚀 How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run ETL
python etl/pipeline.py

### 3. Train Model
python model/train_model.py

### 4. Run Dashboard
python -m streamlit run app/dashboard.py