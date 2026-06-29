from pathlib import Path
import streamlit as st
import pandas as pd


def inject_css(path: str):
    css = Path(path)
    if css.exists():
        st.markdown(f"<style>{css.read_text()}</style>", unsafe_allow_html=True)


def display_metric_card(label, value, delta=None):
    st.metric(label=label, value=value, delta=delta)


def safe_round(value, digits=2):
    try:
        return round(float(value), digits)
    except Exception:
        return value


def dataframe_last_rows(df: pd.DataFrame, n: int = 10):
    if df is None or df.empty:
        return pd.DataFrame()
    return df.tail(n).copy()
