# 🛒 Retail Sales Forecasting & Inventory Optimization System

---

## 📌 Project Overview

This project is an end-to-end retail analytics system that forecasts future product sales and optimizes inventory decisions using machine learning.

---

## 🎯 Problem Statement

Retail businesses face two major challenges:

* ❌ Stockouts → Loss of sales and customer dissatisfaction
* ❌ Overstock → Increased holding cost and blocked capital

This project solves these problems by:

* Predicting future demand using ML models
* Recommending optimal inventory levels

---

## 💡 Business Value

* 📈 Improves demand planning accuracy
* 📦 Reduces stockouts and overstock
* 💰 Optimizes working capital
* ⚡ Enables data-driven inventory decisions

---

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn (Random Forest)
* Matplotlib
* Streamlit

---

## 🧠 Project Workflow

1. Data Loading
2. Feature Engineering (lag_1, lag_2)
3. Model Training (Random Forest)
4. Sales Forecasting (next 7 days)
5. Inventory Optimization
6. Dashboard Visualization

---

## 📂 Project Structure

Retail-Forecasting-System/
│
├── data/
│   └── sales_data.csv
│
├── src/
│   ├── feature_engineering.py
│   ├── model.py
│   ├── forecast.py
│   ├── inventory_advanced.py
│
├── outputs/
│   └── predictions.csv
│
├── app.py
├── main.py
├── generate_data.py
├── requirements.txt
├── README.md
└── .gitignore

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
py main.py
```

### Run Dashboard

```bash
streamlit run app.py
```

---

## 📊 Output

* Sales Forecast
* Inventory Metrics
* Reorder Recommendations

---

## 📸 Screenshots

![Dashboard](images/dashboard.png)
![Forecast](images/forecast.png)
![Inventory](images/inventory.png)

---

## 🔮 Future Improvements

* Multi-store forecasting
* Advanced ML models
* Real-time deployment

---

## 👨‍💻 Author

Siddhesh Pate
Linkdein: www.linkedin.com/in/siddheshpate2007

---

⭐ If you like this project, give it a star!
