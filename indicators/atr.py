def atr(df, period=14):
    high_low = df['High'] - df['Low']
    high_close = (df['High'] - df['Close'].shift()).abs()
    low_close = (df['Low'] - df['Close'].shift()).abs()
    tr = high_low.to_frame('hl')
    tr['hc'] = high_close
    tr['lc'] = low_close
    true_range = tr.max(axis=1)
    return true_range.rolling(period).mean()
