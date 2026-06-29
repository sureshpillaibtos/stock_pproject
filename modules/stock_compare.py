import pandas as pd
import streamlit as st
from services.yahoo_service import get_history
from utils.calculations import calculate_returns, calculate_drawdown, calculate_volatility
from charts.comparison_chart import show_comparison_chart
from charts.heatmap import show_heatmap


def compare_stocks(symbols, period='6mo', interval='1d'):
    frames = []
    summary = []
    closes = {}
    for symbol in symbols:
        df = get_history(symbol, period=period, interval=interval)
        if df.empty:
            continue
        base = df['Close'].iloc[0]
        temp = pd.DataFrame({'Date': df['Date'], 'Symbol': symbol, 'Close': df['Close']})
        temp['Normalized'] = (temp['Close'] / base) * 100
        frames.append(temp)
        returns = calculate_returns(df['Close'])
        drawdown = calculate_drawdown(df['Close'])
        summary.append({
            'Symbol': symbol,
            'Last Close': round(df['Close'].iloc[-1], 2),
            'Return %': round(((df['Close'].iloc[-1] / base) - 1) * 100, 2),
            'Volatility': round(float(calculate_volatility(returns)), 4),
            'Max Drawdown %': round(float(drawdown.min() * 100), 2),
        })
        closes[symbol] = df['Close'].reset_index(drop=True)
    comparison_df = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
    summary_df = pd.DataFrame(summary)
    corr_df = pd.DataFrame(closes).corr() if closes else pd.DataFrame()
    return comparison_df, summary_df, corr_df


def render_compare_section(symbols, period='6mo', interval='1d'):
    st.markdown('### Comparison Section')
    comparison_df, summary_df, corr_df = compare_stocks(symbols, period, interval)
    if comparison_df.empty:
        st.info('Select at least one valid stock for comparison.')
        return
    st.dataframe(summary_df, use_container_width=True, hide_index=True)
    st.plotly_chart(show_comparison_chart(comparison_df), use_container_width=True)
    if not corr_df.empty:
        st.plotly_chart(show_heatmap(corr_df), use_container_width=True)
