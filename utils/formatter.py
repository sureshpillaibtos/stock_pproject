def format_currency(value):
    try:
        return f"${value:,.2f}"
    except Exception:
        return 'N/A'


def format_volume(value):
    try:
        value = float(value)
        if value >= 1_000_000_000:
            return f"{value/1_000_000_000:.2f}B"
        if value >= 1_000_000:
            return f"{value/1_000_000:.2f}M"
        if value >= 1_000:
            return f"{value/1_000:.2f}K"
        return f"{value:.0f}"
    except Exception:
        return 'N/A'


def format_market_cap(value):
    return format_volume(value)
