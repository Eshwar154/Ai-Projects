import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chat_router():
    response = client.get("/chat")
    assert response.status_code == 200

def test_voice_router():
    response = client.get("/voice")
    assert response.status_code == 200

def test_training_router():
    response = client.get("/training")
    assert response.status_code == 200

def test_assessment_router():
    response = client.get("/assessment")
    assert response.status_code == 200