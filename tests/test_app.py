import pytest
from src.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_about(client):
    response = client.get('/about')
    assert response.status_code == 200

def test_contact(client):
    response = client.get('/contact')
    assert response.status_code == 200

def test_api_info(client):
    response = client.get('/api/info')
    assert response.status_code == 200
    assert response.json == {"message": "Welcome to my Flask web app!"}
