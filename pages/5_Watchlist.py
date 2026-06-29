import streamlit as st
from modules.watchlist import render_watchlist_page
from utils.common import inject_css

st.set_page_config(page_title='Watchlist', page_icon='⭐', layout='wide')
inject_css('assets/styles.css')
render_watchlist_page()
