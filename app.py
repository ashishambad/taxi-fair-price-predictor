import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

st.set_page_config(page_title="Taxi Trip Fare Prediction", page_icon="🚕")
BASE_DIR = Path(__file__).resolve().parent
with open(BASE_DIR / "model.pkl", "rb") as f:
    artifact = pickle.load(f)

model, poly = artifact["model"], artifact["poly"]
feature_columns = artifact["feature_columns"]
metrics = artifact["metrics"]

st.title("🚕 Taxi Trip Fare Prediction")
st.write("Predict an estimated taxi trip price using Polynomial Regression.")

st.sidebar.header("Model Performance")
st.sidebar.metric("Test R²", f'{metrics["poly_test_r2"]:.3f}')
st.sidebar.metric("Test MSE", f'{metrics["poly_test_mse"]:.2f}')
st.sidebar.metric("Test RMSE", f'{metrics["poly_test_mse"] ** 0.5:.2f}')

with st.form("prediction_form"):
    c1, c2 = st.columns(2)
    with c1:
        distance = st.number_input("Trip Distance (km)", min_value=0.0, value=10.0, step=0.5)
        passengers = st.number_input("Passenger Count", min_value=1, max_value=10, value=2)
        base = st.number_input("Base Fare", min_value=0.0, value=50.0, step=1.0)
        km_rate = st.number_input("Per Km Rate", min_value=0.0, value=10.0, step=0.5)
        minute_rate = st.number_input("Per Minute Rate", min_value=0.0, value=2.0, step=0.1)
    with c2:
        duration = st.number_input("Trip Duration (minutes)", min_value=0.0, value=20.0, step=1.0)
        time = st.selectbox("Time of Day", ["Morning","Afternoon","Evening","Night"])
        day = st.selectbox("Day of Week", ["Weekday","Weekend"])
        traffic = st.selectbox("Traffic Conditions", ["Low","High","Medium"])
        weather = st.selectbox("Weather", ["Clear","Rain","Snow"])
    submitted = st.form_submit_button("Predict Fare", use_container_width=True)

if submitted:
    row = pd.DataFrame([{
        "Trip_Distance_km": distance, "Time_of_Day": time,
        "Day_of_Week": day, "Passenger_Count": passengers,
        "Traffic_Conditions": traffic, "Weather": weather,
        "Base_Fare": base, "Per_Km_Rate": km_rate,
        "Per_Minute_Rate": minute_rate, "Trip_Duration_Minutes": duration
    }])
    row = pd.get_dummies(row, drop_first=True)
    row = row.reindex(columns=feature_columns, fill_value=False)
    prediction = model.predict(poly.transform(row))[0]
    st.success(f"### Estimated Trip Price: ₹{prediction:,.2f}")

st.divider()
st.caption("Polynomial Regression (degree 2) • Test R²: 0.892 • Test RMSE: 9.49")
