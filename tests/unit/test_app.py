import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from app import app



@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    response = client.get("/")
    assert response.status_code == 200

def test_home_content(client):
    response = client.get("/")
    # Make sure some part of the ASCII art or planet text is present in response
    assert b"+++++++" in response.data or b"planet" in response.data.lower()

def test_about_status_code(client):
    response = client.get("/about")
    assert response.status_code == 200

def test_about_content(client):
    response = client.get("/about")
    assert b"Planet App" in response.data

def test_api_planet(client):
    response = client.get("/api/planet")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Earth"
    assert data["type"] == "Terrestrial"
    assert data["moons"] == 1
    assert "description" in data
