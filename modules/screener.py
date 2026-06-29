import streamlit as st
import pandas as pd
from config.categories import CATEGORIES
from modules.scoring import rank_category


def render_screener_page():
    st.title('Stock Screener')
    category = st.selectbox('Category', list(CATEGORIES.keys()))
    df = rank_category(CATEGORIES[category])
    min_score = st.slider('Minimum Score', min_value=float(df['Score'].min()), max_value=float(df['Score'].max()), value=float(df['Score'].min()))
    filtered = df[df['Score'] >= min_score]
    st.dataframe(filtered, use_container_width=True, hide_index=True)
