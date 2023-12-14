import pytest
from pathlib import Path
from .fixtures import client
from unittest.mock import patch
from werkzeug.datastructures import FileStorage


@pytest.fixture(autouse=True)
def mock_auth():
    with patch("collector.auth.get_tokens", return_value=["1"]) as auth:
        yield auth


@pytest.fixture
def mocked_payload():
    path = Path(__file__).parent
    files_generator = path.rglob("*idealista*.html")
    if file := next(files_generator):
        return FileStorage(
            stream=open(file, "rb"),
            name=file.name,
            filename=file,
            content_type="text/html"
        )

@patch("werkzeug.datastructures.FileStorage.save")
def test_file_upload(savefile, client, mocked_payload):
    response = client.post(
        "/upload-page",
        data={"file": mocked_payload},
        headers={
            "Authorization": "Bearer 1"
        }
    )
    assert response.status_code == 200
    assert savefile.called
