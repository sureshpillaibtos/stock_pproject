import pandas as pd
import streamlit as st
from services.market_service import get_market_overview


def render_market_overview():
    st.markdown("### Market Overview")
    rows = get_market_overview()
    cols = st.columns(len(rows) if rows else 1)
    for i, row in enumerate(rows):
        cols[i].metric(row['Index'], f"{row['Close']:.2f}", f"{row['Change %']:.2f}%")
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
