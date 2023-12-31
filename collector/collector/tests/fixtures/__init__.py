import pytest

@pytest.fixture
def client():
    from collector.main import app
    app.config['TESTING'] = True
    app.config['UPLOAD_FOLDER'] = ""
    with app.test_client() as client:
        yield client
