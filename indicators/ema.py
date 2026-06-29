def ema(series, window):
    return series.ewm(span=window, adjust=False).mean()
