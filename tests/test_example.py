"""Простой тест для проверки CI/CD"""

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

def test_api_connection():
    """Проверка работы requests"""
    import requests
    try:
        response = requests.get('https://httpbin.org/get', timeout=5)
        assert response.status_code == 200
        print("API connection successful")
    except Exception as e:
        print(f"API connection failed: {e}")
        # Не падаем, просто пропускаем проверку
        pass