import pandas as pd

def forecast_future(model, last_values, days=7):

    future_preds = []

    lag_1, lag_2 = last_values

    for i in range(days):

        input_df = pd.DataFrame([[lag_1, lag_2]], columns=['lag_1', 'lag_2'])

        pred = model.predict(input_df)[0]

        future_preds.append(pred)

        # shift values
        lag_2 = lag_1
        lag_1 = pred

    print("\nFuture Predictions (Next 7 Days):")
    print(future_preds)

    return future_preds