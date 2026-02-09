import pytest

def test_addition():
    """Простой тест сложения"""
    assert 1 + 1 == 2

def test_subtraction():
    """Простой тест вычитания"""
    assert 5 - 3 == 2

def test_multiplication():
    """Простой тест умножения"""
    assert 2 * 3 == 6

class TestMathOperations:
    """Класс с тестами математических операций"""
    
    def test_division(self):
        """Тест деления"""
        assert 10 / 2 == 5
    
    def test_power(self):
        """Тест возведения в степень"""
        assert 2 ** 3 == 8

@pytest.mark.api
def test_api_endpoint():
    """Пример API теста"""
    import requests
    response = requests.get('https://httpbin.org/get')
    assert response.status_code == 200
    assert 'headers' in response.json()

@pytest.mark.ui
def test_ui_element():
    """Пример UI теста"""
    # Здесь будет код Selenium
    assert True  # Заглушка