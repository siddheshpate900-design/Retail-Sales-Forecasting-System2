# 🛒 Retail Sales Forecasting & Inventory Optimization System

## 📌 Project Overview

This project is an end-to-end retail analytics system that forecasts future product sales and optimizes inventory decisions using machine learning.

The system uses historical sales data to predict future demand and calculates key inventory metrics such as **Safety Stock**, **Reorder Point**, and **Order Quantity** to help businesses maintain optimal stock levels.

---

## 🎯 Problem Statement

Retail businesses often face two major challenges:

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

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn (Random Forest)
* Matplotlib
* Streamlit

---

## 🧠 Project Workflow

1. **Data Loading**

   * Load historical sales dataset

2. **Feature Engineering**

   * Create lag features (lag_1, lag_2)

3. **Model Training**

   * Train Random Forest Regressor

4. **Sales Forecasting**

   * Predict future sales (next 7 days)

5. **Inventory Optimization**

   * Calculate:

     * Demand during Lead Time
     * Safety Stock
     * Reorder Point
     * Order Quantity

6. **Dashboard**

   * Visualize predictions and inventory decisions

---

## 📂 Project Structure

```
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
```

---

## ⚙️ Installation & Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/Retail-Sales-Forecasting-System.git
cd Retail-Sales-Forecasting-System
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Run Main Script

```bash
py main.py
```

### Run Dashboard

```bash
streamlit run app.py
```

---

## 📊 Output

### ✔ Sales Forecast

* Predicts next 7 days sales

### ✔ Inventory Metrics

* Demand during Lead Time
* Safety Stock
* Reorder Point
* Order Quantity

---

## 📸 Screenshots

### Dashboard

![Dashboard](images/dashboard.png)

### Forecast Graph

![Forecast](images/forecast.png)

### Inventory Output

![Inventory](images/inventory.png)

---

## 🔮 Future Improvements

* Multi-product & multi-store forecasting
* Advanced models (XGBoost, ARIMA, LSTM)
* Real-time API deployment
* Price & promotion impact analysis
* Automated reorder system

---

## 📚 Learning Outcomes

* Time series forecasting basics
* Feature engineering for ML
* Inventory optimization logic
* Building interactive dashboards
* End-to-end project development

---

## 👨‍💻 Author

**Siddhesh Pate**

Linkdein: www.linkedin.com/in/siddheshpate2007

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
