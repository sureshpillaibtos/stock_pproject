import plotly.express as px


def show_volume(df, symbol):
    fig = px.bar(df, x='Date', y='Volume', title=f'{symbol} Volume', template='plotly_dark')
    fig.update_layout(height=320)
    return fig
