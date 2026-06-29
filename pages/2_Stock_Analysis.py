import streamlit as st
from config.categories import CATEGORIES
from config.constants import PERIOD_OPTIONS, INTERVAL_OPTIONS, CHART_OPTIONS, INDICATOR_OPTIONS
from modules.stock_analysis import render_stock_analysis
from utils.common import inject_css

st.set_page_config(page_title='Stock Analysis', page_icon='📊', layout='wide')
inject_css('assets/styles.css')
st.title('Stock Analysis')
symbol = st.selectbox('Stock', sorted({s for v in CATEGORIES.values() for s in v}))
period = st.selectbox('Period', PERIOD_OPTIONS, index=2)
interval = st.selectbox('Interval', INTERVAL_OPTIONS, index=0)
chart_type = st.selectbox('Chart Type', CHART_OPTIONS)
indicators = st.multiselect('Indicators', INDICATOR_OPTIONS, default=['SMA20', 'SMA50', 'RSI'])
render_stock_analysis(symbol, period, interval, chart_type, indicators)
