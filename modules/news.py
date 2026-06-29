import streamlit as st

def render_news_placeholder(symbol):
    st.markdown('### News')
    st.info(f'News module placeholder for {symbol}. This can be extended with RSS or public news APIs later.')
