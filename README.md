# Stock Research Platform Dashboard

A polished multi-page Streamlit application for researching US equities using free Yahoo Finance data.

## Features
- Multi-page Streamlit layout.
- Category-based stock discovery.
- Market overview with S&P 500, Nasdaq, Dow Jones, VIX, DXY, and US 10Y.
- Single stock analysis with today's summary.
- Previous 10 trading days OHLCV table.
- Reusable chart engine for candlestick, line, OHLC, volume, RSI, MACD, and Bollinger Bands.
- Stock comparison engine with normalized returns, volatility, drawdown, and relative performance.
- Modular project structure for future AI research enhancements.

## Categories
- Standard Stocks: MSFT, GOOGL, AAPL, AMZN, META, TSLA
- AI Infrastructure: NVDA, AVGO, TSM, MU
- Traditional Semiconductors: INTC, AMD, QCOM, TXN
- Networking & Data Center: ANET, MRVL, AVGO
- Foundries: TSM, GFS

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Multi-page navigation
- Dashboard
- Stock Analysis
- Compare Stocks
- Stock Screener
- Watchlist
- Settings

## Notes
- Data source: Yahoo Finance through `yfinance`.
- Caching is enabled using Streamlit cache decorators.
- The scoring model is intentionally simple and easy to extend.
- The future AI research module can consume outputs from services, indicators, and scoring modules.
# stock_pproject
