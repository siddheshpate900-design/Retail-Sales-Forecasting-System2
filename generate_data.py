import pandas as pd
import numpy as np

dates = pd.date_range(start="2023-01-01", periods=100)

sales = []

base = 20

for i in range(100):
    trend = i * 0.3
    noise = np.random.randint(-5, 5)
    value = base + trend + noise
    sales.append(max(0, int(value)))

df = pd.DataFrame({
    "date": dates,
    "product_id": 101,
    "sales": sales
})

df.to_csv("data/sales_data.csv", index=False)

print("New dataset generated!")