import pytest
from pathlib import Path
from .fixtures import client
from unittest.mock import patch


@pytest.fixture(autouse=True)
def mock_auth():
    with patch("collector.auth.get_tokens", return_value=["1"]) as auth:
        yield auth


@pytest.fixture
def mocked_file_to_upload():
    path = Path(__file__).parent
    files_generator = path.rglob("*idealista*.html")
    if file := next(files_generator):
        return open(file, "r").read()


@patch("builtins.open")
def test_file_upload(open, client, mocked_file_to_upload):
    response = client.post(
        "/upload-page",
        data={"file": mocked_file_to_upload},
        headers={
            "Content-Type": "multipart/form-data",
            "Authorization": "Bearer 1"
        }
    )
    assert response.status_code == 200
    assert open.called
