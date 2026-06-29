from config.constants import INDEX_TICKERS
from services.yahoo_service import get_history
from utils.calculations import calculate_percentage


def get_market_overview():
    rows = []
    for label, symbol in INDEX_TICKERS.items():
        df = get_history(symbol, period='1mo', interval='1d')
        if df.empty:
            continue
        latest = df.iloc[-1]
        prev = df.iloc[-2] if len(df) > 1 else latest
        change_pct = calculate_percentage(latest['Close'], prev['Close'])
        rows.append({
            'Index': label,
            'Symbol': symbol,
            'Close': latest['Close'],
            'Change %': change_pct,
            'Volume': latest.get('Volume', None),
        })
    return rows
