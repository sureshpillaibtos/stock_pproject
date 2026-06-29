def validate_symbol(symbol: str) -> bool:
    return isinstance(symbol, str) and 0 < len(symbol.strip()) <= 10
