from indicators.moving_average import sma

def test_sma_exists():
    assert callable(sma)
