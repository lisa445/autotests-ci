def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

def test_api():
    import requests
    response = requests.get('https://httpbin.org/get', timeout=5)
    assert response.status_code == 200