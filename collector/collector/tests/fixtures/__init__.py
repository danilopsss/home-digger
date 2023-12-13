import pytest

@pytest.fixture
def client():
    from collector.app import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
