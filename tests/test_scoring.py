from modules.scoring import score_stock

def test_score_stock_callable():
    assert callable(score_stock)
