import streamlit as st
from services.yahoo_service import get_history, get_ticker_info
from modules.indicators import apply_indicators
from modules.charts import show_ohlc
from charts.candlestick import show_candlestick
from charts.line_chart import show_line_chart
from charts.volume_chart import show_volume
from modules.technical_analysis import render_technical_section
from modules.company_profile import render_company_profile
from modules.financials import render_financial_summary
from utils.formatter import format_currency, format_volume


def render_stock_analysis(symbol, period, interval, chart_type, indicators):
    df = get_history(symbol, period=period, interval=interval)
    if df.empty:
        st.warning(f'No data available for {symbol}')
        return
    df = apply_indicators(df)
    info = get_ticker_info(symbol)
    latest = df.iloc[-1]
    prev = df.iloc[-2] if len(df) > 1 else latest
    st.markdown('### Today's Summary')
    c1, c2, c3, c4 = st.columns(4)
    c1.metric('Close', format_currency(latest['Close']), f"{((latest['Close']-prev['Close'])/prev['Close'])*100:.2f}%")
    c2.metric('Open', format_currency(latest['Open']))
    c3.metric('Day Range', f"{latest['Low']:.2f} - {latest['High']:.2f}")
    c4.metric('Volume', format_volume(latest.get('Volume', 0)))
    st.markdown('### Price Chart')
    if chart_type == 'Candlestick':
        st.plotly_chart(show_candlestick(df, symbol), use_container_width=True)
    elif chart_type == 'Line':
        st.plotly_chart(show_line_chart(df, symbol), use_container_width=True)
    else:
        st.plotly_chart(show_ohlc(df, symbol), use_container_width=True)
    st.plotly_chart(show_volume(df, symbol), use_container_width=True)
    st.markdown("### Previous 10 Trading Days")
    cols = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    available = [c for c in cols if c in df.columns]
    st.dataframe(df[available].tail(10).sort_values('Date', ascending=False), use_container_width=True, hide_index=True)
    render_technical_section(df, symbol, indicators)
    render_financial_summary(symbol)
    render_company_profile(symbol)
