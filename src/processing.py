
def generate_signal(df, window):
    df["rolling_mean"] = df["close"].rolling(window).mean()

    df["signal"] = (df["close"] > df["rolling_mean"]).astype(int)
    return df

