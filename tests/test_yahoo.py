from services.yahoo_service import get_history

def test_yahoo_service_callable():
    assert callable(get_history)
