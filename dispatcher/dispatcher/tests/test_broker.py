import json
import pytest

from .fixtures import *
from unittest.mock import patch
from pika.adapters.blocking_connection import BlockingConnection


@pytest.fixture
def mocked_payload():
    return json.dumps({
        "broker": "rabbitmq",
        "file": "file_name.ext",
        "event": "created"
    })


@pytest.fixture(autouse=True)
def mock_auth():
    with patch("dispatcher.auth.get_tokens", return_value=["1"]) as auth:
        yield auth


@patch("dispatcher.core.broker.utils.Broker.rabbitmq_connection", return_value=BlockingConnection)
def test_deliver_message(rabbit, client, mocked_payload):
    response = client.post("/dispatcher/deliver", data=mocked_payload, headers={"Authorization": "Bearer 1", "Content-Type": "application/json"})
    assert response.status_code == 202
    assert response.json == {
        "file": "file_name.ext",
        "event": "created"
    }


