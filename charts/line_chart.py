import plotly.express as px


def show_line_chart(df, symbol):
    fig = px.line(df, x='Date', y='Close', title=f'{symbol} Close Price', template='plotly_dark')
    fig.update_layout(height=520)
    return fig
