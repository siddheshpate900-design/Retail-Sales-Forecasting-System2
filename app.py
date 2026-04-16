import streamlit as st
import pandas as pd
from src.model import train_model
from src.feature_engineering import create_features
from src.forecast import forecast_future
from src.inventory_advanced import advanced_inventory

st.title("🛒 Retail Forecasting & Inventory Dashboard")

# Load data
df = pd.read_csv("data/sales_data.csv", parse_dates=["date"])

st.subheader("📊 Raw Data")
st.write(df.tail())

# Feature engineering
df = create_features(df)

# Train model
model, preds = train_model(df)

# Future forecast
last_values = [
    df['sales'].iloc[-1],
    df['sales'].iloc[-2]
]

future_preds = forecast_future(model, last_values)

# User Inputs
st.sidebar.header("⚙️ Inventory Settings")
lead_time = st.sidebar.slider("Lead Time (days)", 1, 10, 3)
on_hand = st.sidebar.number_input("Current Stock", value=50)

# Inventory Calculation
inventory = advanced_inventory(
    future_preds,
    lead_time=lead_time,
    on_hand=on_hand
)

# Display Forecast
st.subheader("📈 Future Sales Prediction")
future_df = pd.DataFrame({
    "Day": range(1, len(future_preds)+1),
    "Predicted Sales": future_preds
})
st.line_chart(future_df.set_index("Day"))

# Display Inventory Results
st.subheader("📦 Inventory Recommendation")

st.write(f"**Demand during Lead Time:** {inventory['demand_lead_time']}")
st.write(f"**Safety Stock:** {inventory['safety_stock']}")
st.write(f"**Reorder Point:** {inventory['reorder_point']}")
st.write(f"**Order Quantity:** {inventory['order_qty']}")