from sklearn.ensemble import RandomForestRegressor
import pandas as pd

def train_model(df):

    X = df[['lag_1', 'lag_2']]
    y = df['sales']

    model = RandomForestRegressor()
    model.fit(X, y)

    predictions = model.predict(X)

    # Save predictions
    output = df.copy()
    output['predictions'] = predictions
    output.to_csv("outputs/predictions.csv", index=False)

    print("Model Trained")
    print("Predictions:", predictions)
    print("Predictions saved to outputs folder")

    return model, predictions