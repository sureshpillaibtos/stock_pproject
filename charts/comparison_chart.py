import plotly.express as px


def show_comparison_chart(df):
    fig = px.line(df, x='Date', y='Normalized', color='Symbol', title='Normalized Stock Comparison', template='plotly_dark')
    fig.update_layout(height=520)
    return fig
