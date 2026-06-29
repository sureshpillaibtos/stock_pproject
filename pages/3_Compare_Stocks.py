import streamlit as st
from config.categories import CATEGORIES
from config.constants import PERIOD_OPTIONS, INTERVAL_OPTIONS
from modules.stock_compare import render_compare_section
from utils.common import inject_css

st.set_page_config(page_title='Compare Stocks', page_icon='⚖️', layout='wide')
inject_css('assets/styles.css')
st.title('Compare Stocks')
all_symbols = sorted({s for v in CATEGORIES.values() for s in v})
symbols = st.multiselect('Select symbols', all_symbols, default=['MSFT', 'NVDA', 'TSM'])
period = st.selectbox('Period', PERIOD_OPTIONS, index=2)
interval = st.selectbox('Interval', INTERVAL_OPTIONS, index=0)
if st.button('Analyse', type='primary'):
    render_compare_section(symbols, period, interval)
