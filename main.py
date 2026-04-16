from src.data_preprocessing import load_data
from src.feature_engineering import create_features
from src.model import train_model
from src.inventory import inventory_calc
from src.visualization import plot_sales 
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from src.forecast import forecast_future
from src.inventory_advanced import advanced_inventory 


df = load_data("data/sales_data.csv")
df = create_features(df)

model, preds = train_model(df)
plot_sales(df, preds)

inventory_calc(preds)
last_values = [
    df['sales'].iloc[-1],   # lag_1
    df['sales'].iloc[-2]    # lag_2
]

future_preds = forecast_future(model, last_values)
advanced_inventory(future_preds)