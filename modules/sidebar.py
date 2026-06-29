import streamlit as st
from config.categories import CATEGORIES
from config.constants import PERIOD_OPTIONS, INTERVAL_OPTIONS, CHART_OPTIONS, INDICATOR_OPTIONS
from config.settings import DEFAULT_PERIOD, DEFAULT_INTERVAL, DEFAULT_CHART


def render_sidebar():
    st.sidebar.title('Stock Research Controls')
    category = st.sidebar.selectbox('Stock Category', list(CATEGORIES.keys()))
    stock = st.sidebar.selectbox('Stock', CATEGORIES[category])
    period = st.sidebar.radio('Period', PERIOD_OPTIONS, index=PERIOD_OPTIONS.index(DEFAULT_PERIOD))
    interval = st.sidebar.radio('Interval', INTERVAL_OPTIONS, index=INTERVAL_OPTIONS.index(DEFAULT_INTERVAL))
    chart_type = st.sidebar.radio('Chart', CHART_OPTIONS, index=CHART_OPTIONS.index(DEFAULT_CHART))
    indicators = st.sidebar.multiselect('Indicators', INDICATOR_OPTIONS, default=['SMA20', 'SMA50', 'SMA200'])
    compare_symbols = st.sidebar.multiselect('Compare Stocks', sorted({s for v in CATEGORIES.values() for s in v}), default=['MSFT', 'NVDA'])
    analyse = st.sidebar.button('Analyse', type='primary', use_container_width=True)
    return {
        'category': category,
        'stock': stock,
        'period': period,
        'interval': interval,
        'chart_type': chart_type,
        'indicators': indicators,
        'compare_symbols': compare_symbols,
        'analyse': analyse,
    }
