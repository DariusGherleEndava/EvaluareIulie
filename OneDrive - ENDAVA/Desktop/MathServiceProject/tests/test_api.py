import sys
import os
import pytest
from fastapi.testclient import TestClient

# Add the parent directory to sys.path so 'app' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app

client = TestClient(app)

def test_pow():
    response = client.post("/pow", json={"base": 2, "exponent": 8})
    assert response.status_code == 200
    assert response.json()["result"] == 256

def test_fibonacci():
    response = client.post("/fibonacci", json={"n": 10})
    assert response.status_code == 200
    assert response.json()["result"] == 55

def test_factorial():
    response = client.post("/factorial", json={"n": 5})
    assert response.status_code == 200
    assert response.json()["result"] == 120

def test_logs():
    response = client.get("/logs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
