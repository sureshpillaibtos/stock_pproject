import plotly.graph_objects as go
from charts.candlestick import show_candlestick
from charts.line_chart import show_line_chart
from charts.volume_chart import show_volume
from charts.comparison_chart import show_comparison_chart
from charts.heatmap import show_heatmap


def show_ohlc(df, symbol):
    fig = go.Figure(data=[go.Ohlc(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name=symbol)])
    fig.update_layout(template='plotly_dark', title=f'{symbol} OHLC', xaxis_rangeslider_visible=False, height=520)
    return fig


def show_rsi(df, symbol):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['RSI'], mode='lines', name='RSI'))
    fig.add_hline(y=70, line_dash='dash')
    fig.add_hline(y=30, line_dash='dash')
    fig.update_layout(template='plotly_dark', title=f'{symbol} RSI', height=300)
    return fig


def show_macd(df, symbol):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['MACD'], mode='lines', name='MACD'))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['MACD_SIGNAL'], mode='lines', name='Signal'))
    fig.add_trace(go.Bar(x=df['Date'], y=df['MACD_HIST'], name='Histogram'))
    fig.update_layout(template='plotly_dark', title=f'{symbol} MACD', height=320)
    return fig


def show_bollinger(df, symbol):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], mode='lines', name='Close'))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['BB_UPPER'], mode='lines', name='Upper'))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['BB_MID'], mode='lines', name='Middle'))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['BB_LOWER'], mode='lines', name='Lower'))
    fig.update_layout(template='plotly_dark', title=f'{symbol} Bollinger Bands', height=320)
    return fig
