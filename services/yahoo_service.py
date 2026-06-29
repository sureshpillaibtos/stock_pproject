import pandas as pd
import streamlit as st
import yfinance as yf


@st.cache_data(ttl=900)
def get_history(symbol: str, period: str = '6mo', interval: str = '1d') -> pd.DataFrame:
    df = yf.download(symbol, period=period, interval=interval, auto_adjust=False, progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [c[0] for c in df.columns]
    df = df.reset_index()
    if 'Date' not in df.columns and 'Datetime' in df.columns:
        df.rename(columns={'Datetime': 'Date'}, inplace=True)
    return df


@st.cache_data(ttl=1800)
def get_ticker_info(symbol: str) -> dict:
    try:
        info = yf.Ticker(symbol).info
        return info if isinstance(info, dict) else {}
    except Exception:
        return {}


@st.cache_data(ttl=900)
def get_fast_info(symbol: str) -> dict:
    try:
        fi = dict(yf.Ticker(symbol).fast_info)
        return fi
    except Exception:
        return {}
