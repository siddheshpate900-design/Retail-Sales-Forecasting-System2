import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # convert date column
    df['date'] = pd.to_datetime(df['date'])

    print("Data Loaded Successfully")
    print(df.head())

    return df