import streamlit as st


def render_watchlist_page():
    st.title('Watchlist')
    if 'watchlist' not in st.session_state:
        st.session_state.watchlist = ['MSFT', 'NVDA', 'TSM']
    st.write('Current watchlist symbols:')
    st.dataframe({'Symbol': st.session_state.watchlist}, use_container_width=True, hide_index=True)
