import matplotlib.pyplot as plt

def plot_sales(df, preds):
    plt.figure()

    # Actual sales
    plt.plot(df['date'], df['sales'], label='Actual Sales')

    # Predicted sales
    plt.plot(df['date'], preds, label='Predicted Sales')

    plt.title("Sales Forecast vs Actual")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()

    plt.show()