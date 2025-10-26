import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Welcome to CI/CD Demo!"
    assert data['status'] == "running"

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == "healthy"

def test_add(client):
    response = client.get('/add/5/3')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 8
    assert data['operation'] == "addition"

def test_add_large_numbers(client):
    response = client.get('/add/100/200')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 300
    assert data['operation'] == "addition"