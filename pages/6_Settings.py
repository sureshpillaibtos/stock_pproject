import streamlit as st
from utils.common import inject_css

st.set_page_config(page_title='Settings', page_icon='⚙️', layout='wide')
inject_css('assets/styles.css')
st.title('Settings')
st.write('Reserved for cache controls, theme settings, export defaults, and future AI module toggles.')
