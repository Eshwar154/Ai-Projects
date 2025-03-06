import pytest

@pytest.fixture(scope='session')
def setup():
    # Setup code can be added here
    yield
    # Teardown code can be added here