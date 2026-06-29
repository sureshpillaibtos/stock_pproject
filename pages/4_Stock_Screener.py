import streamlit as st
from modules.screener import render_screener_page
from utils.common import inject_css

st.set_page_config(page_title='Stock Screener', page_icon='🧮', layout='wide')
inject_css('assets/styles.css')
render_screener_page()
