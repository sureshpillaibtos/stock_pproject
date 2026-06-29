import streamlit as st
from services.yahoo_service import get_ticker_info
from utils.formatter import format_currency, format_market_cap


def render_financial_summary(symbol):
    info = get_ticker_info(symbol)
    st.markdown('### Financial Summary')
    data = {
        'Market Cap': format_market_cap(info.get('marketCap')),
        'Trailing PE': info.get('trailingPE', 'N/A'),
        'Forward PE': info.get('forwardPE', 'N/A'),
        'EPS': info.get('trailingEps', 'N/A'),
        'Revenue': format_currency(info.get('totalRevenue')) if info.get('totalRevenue') else 'N/A',
        'Gross Margins': info.get('grossMargins', 'N/A'),
        'Operating Margins': info.get('operatingMargins', 'N/A'),
    }
    st.dataframe(data, use_container_width=True)
