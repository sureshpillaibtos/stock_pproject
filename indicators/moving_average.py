def sma(series, window):
    return series.rolling(window).mean()
