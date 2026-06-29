import streamlit as st
from modules.charts import show_rsi, show_macd, show_bollinger


def render_technical_section(df, symbol, indicators):
    st.markdown('### Technical Indicators')
    if 'RSI' in indicators:
        st.plotly_chart(show_rsi(df, symbol), use_container_width=True)
    if 'MACD' in indicators:
        st.plotly_chart(show_macd(df, symbol), use_container_width=True)
    if 'Bollinger Bands' in indicators:
        st.plotly_chart(show_bollinger(df, symbol), use_container_width=True)
