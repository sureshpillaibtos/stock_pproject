import streamlit as st
from config.categories import CATEGORIES
from modules.sidebar import render_sidebar
from modules.market_overview import render_market_overview
from modules.scoring import rank_category
from modules.stock_analysis import render_stock_analysis
from modules.stock_compare import render_compare_section


def render_dashboard():
    st.markdown('<div class="page-title">Stock Research Platform Dashboard</div>', unsafe_allow_html=True)
    st.caption('Category-driven stock research, technical analysis, and comparison using Yahoo Finance data.')
    controls = render_sidebar()
    render_market_overview()
    st.markdown('### Top Stocks in Selected Category')
    ranked = rank_category(CATEGORIES[controls['category']])
    st.dataframe(ranked, use_container_width=True, hide_index=True)
    st.markdown('---')
    render_stock_analysis(controls['stock'], controls['period'], controls['interval'], controls['chart_type'], controls['indicators'])
    st.markdown('---')
    render_compare_section(controls['compare_symbols'], controls['period'], controls['interval'])
