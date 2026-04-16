def create_features(df):
    df = df.sort_values("date")

    df['lag_1'] = df['sales'].shift(1)
    df['lag_2'] = df['sales'].shift(2)

    df = df.dropna()

    print("Features Created")
    print(df.head())

    return df