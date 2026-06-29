import numpy as np
import pandas as pd


def calculate_percentage(current, previous):
    if previous in [0, None] or pd.isna(previous):
        return np.nan
    return ((current - previous) / previous) * 100


def calculate_returns(close_series):
    return close_series.pct_change().fillna(0)


def calculate_drawdown(close_series):
    running_max = close_series.cummax()
    return (close_series / running_max) - 1


def calculate_volatility(returns, annualization=252):
    return returns.std() * np.sqrt(annualization)
