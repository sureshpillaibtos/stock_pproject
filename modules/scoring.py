import pandas as pd
from services.yahoo_service import get_history
from modules.indicators import apply_indicators


def score_stock(symbol: str):
    df = get_history(symbol, period='6mo', interval='1d')
    if df.empty or len(df) < 30:
        return {'Symbol': symbol, 'Score': 0}
    df = apply_indicators(df)
    latest = df.iloc[-1]
    one_month_ago = df.iloc[max(0, len(df)-22)]
    momentum = ((latest['Close'] - one_month_ago['Close']) / one_month_ago['Close']) * 100 if one_month_ago['Close'] else 0
    trend = 0
    trend += 1 if latest['Close'] > latest.get('SMA20', latest['Close']) else 0
    trend += 1 if latest['Close'] > latest.get('SMA50', latest['Close']) else 0
    volume_score = df['Volume'].tail(20).mean() / 1_000_000
    total = round(momentum * 0.6 + trend * 10 + volume_score * 0.1, 2)
    return {
        'Symbol': symbol,
        'Close': latest['Close'],
        '1M Return %': round(momentum, 2),
        'Trend Score': trend,
        'Avg Volume (20D)': round(df['Volume'].tail(20).mean(), 0),
        'Score': total,
    }


def rank_category(symbols):
    data = [score_stock(s) for s in symbols]
    return pd.DataFrame(data).sort_values('Score', ascending=False).reset_index(drop=True)
