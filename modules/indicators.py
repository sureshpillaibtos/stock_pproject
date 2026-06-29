from indicators.moving_average import sma
from indicators.ema import ema
from indicators.rsi import rsi
from indicators.macd import macd
from indicators.bollinger import bollinger_bands


def apply_indicators(df):
    if df.empty:
        return df
    out = df.copy()
    out['SMA20'] = sma(out['Close'], 20)
    out['SMA50'] = sma(out['Close'], 50)
    out['SMA200'] = sma(out['Close'], 200)
    out['EMA20'] = ema(out['Close'], 20)
    out['RSI'] = rsi(out['Close'])
    macd_line, signal_line, hist = macd(out['Close'])
    out['MACD'] = macd_line
    out['MACD_SIGNAL'] = signal_line
    out['MACD_HIST'] = hist
    bb_mid, bb_upper, bb_lower = bollinger_bands(out['Close'])
    out['BB_MID'] = bb_mid
    out['BB_UPPER'] = bb_upper
    out['BB_LOWER'] = bb_lower
    return out
