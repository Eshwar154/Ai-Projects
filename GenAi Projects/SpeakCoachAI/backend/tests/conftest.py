import pytest
from unittest.mock import MagicMock
from backend import config, database  # Adjust import paths as needed

@pytest.fixture
def mock_openai(mocker):
    """Mocks the OpenAI API."""
    mock = MagicMock()
    mocker.patch("backend.chat.openai.Completion.create", new=mock)  # Adjust path
    return mock

@pytest.fixture
def test_db():
    """Provides a test database session."""
    # Replace with your actual database setup for testing
    # This is a simplified example using an in-memory SQLite database
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from backend.database import Base  # Adjust import path

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()