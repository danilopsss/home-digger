import pytest


@pytest.fixture
def client():
    from dispatcher.main import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
