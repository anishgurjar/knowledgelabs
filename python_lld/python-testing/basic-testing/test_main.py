from main import get_weather

def test_get_weather():
    assert get_weather(22) == "hot"
    assert get_weather(18) == "cold"
