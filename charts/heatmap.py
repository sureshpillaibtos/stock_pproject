import plotly.express as px


def show_heatmap(corr_df):
    fig = px.imshow(corr_df, text_auto=True, aspect='auto', color_continuous_scale='Tealgrn', title='Correlation Heatmap')
    fig.update_layout(height=520)
    return fig
