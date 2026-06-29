import plotly.graph_objects as go


def show_candlestick(df, symbol):
    fig = go.Figure(data=[go.Candlestick(
        x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name=symbol
    )])
    fig.update_layout(template='plotly_dark', title=f'{symbol} Candlestick', xaxis_rangeslider_visible=False, height=520)
    return fig
