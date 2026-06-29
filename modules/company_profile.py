import streamlit as st
from services.yahoo_service import get_ticker_info
from utils.formatter import format_market_cap


def render_company_profile(symbol):
    info = get_ticker_info(symbol)
    st.markdown('### Company Profile')
    c1, c2, c3 = st.columns(3)
    c1.metric('Sector', info.get('sector', 'N/A'))
    c2.metric('Industry', info.get('industry', 'N/A'))
    c3.metric('Market Cap', format_market_cap(info.get('marketCap')))
    st.write(info.get('longBusinessSummary', 'Business summary not available.'))
