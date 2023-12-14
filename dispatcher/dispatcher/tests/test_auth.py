import pytest
from .fixtures import client
from unittest.mock import patch


@pytest.fixture(autouse=True)
def mock_auth():
    with patch("dispatcher.auth.get_tokens", return_value=["1"]) as auth:
        yield auth


def test_authorized_ping(client):
    response = client.get("/internal/ping", headers={"Authorization": "Bearer 1"})
    assert response.status_code == 200
    assert response.json.get("response") == "pong"


def test_not_authorized_ping(client):
    response = client.get("/internal/ping", headers={"Authorization": "Bearer 1112233"})
    assert response.status_code == 401
