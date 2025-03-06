import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_response(user_input: str, role: str = "user"):
    """
    Generates a response from the LLM based on the user input and role.
    """
    # Replace this with your actual LLM API call
    return f"AI Response: {user_input} (Role: {role})"

from fastapi.testclient import TestClient
from backend.main import app  # Assuming your FastAPI app instance is in main.py
from backend import chat  # Adjust import path
from unittest.mock import patch

client = TestClient(app)  # Create a test client

def test_chat_with_ai_success():
    """Tests successful chat with AI."""
    response = client.post("/chat/", json={"text": "Hello, AI!"})
    assert response.status_code == 200
    assert "response" in response.json()
    assert "AI Response: Hello, AI! (Role: coach)" in response.json()["response"]

@patch("backend.chat.generate_response")  # Adjust import path
def test_chat_with_ai_mocked(mock_generate_response):
    """Tests successful chat with AI using a mocked generate_response function."""
    mock_generate_response.return_value = "Mocked AI Response"
    response = client.post("/chat/", json={"text": "Hello, AI!"})
    assert response.status_code == 200
    assert "response" in response.json()
    assert response.json()["response"] == "Mocked AI Response"
    mock_generate_response.assert_called_once_with("Hello, AI!", role="coach")

def test_chat_with_ai_empty_input():
    """Tests handling of empty input."""
    response = client.post("/chat/", json={"text": ""})
    assert response.status_code == 200  # Or appropriate error code
    assert "response" in response.json()
    # Add more specific assertions based on how your app handles empty input

import { fetchData } from './api';

jest.mock('./api'); // Mock the api module

test('fetches data successfully', async () => {
  const mockData = { message: 'Hello, world!' };
  fetchData.mockResolvedValue(mockData);

  const data = await fetchData();
  expect(data).toEqual(mockData);
});

test('handles API errors', async () => {
  fetchData.mockRejectedValue(new Error('API Error'));

  await expect(fetchData()).rejects.toThrow('API Error');
});
