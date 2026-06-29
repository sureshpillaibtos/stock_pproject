import streamlit as st
from config.settings import APP_TITLE, PAGE_ICON, LAYOUT
from modules.dashboard import render_dashboard
from utils.common import inject_css

st.set_page_config(page_title=APP_TITLE, page_icon=PAGE_ICON, layout=LAYOUT)
inject_css('assets/styles.css')
render_dashboard()
