import pytest

from pathlib import Path
from unittest.mock import patch
from homedigger.core.scrapper import Scrapper


@pytest.fixture
def mock_page():
    path = Path(__file__).parent
    files_generator = path.rglob("*.html")
    return files_generator


@pytest.fixture(autouse=True)
def mock_providers_register():
    register = "homedigger.core.scrapper.PROVIDERS_REGISTER"
    new_value = ["SomeProvider1", "SomeProvider2"]
    with patch(register, new=new_value):
        yield


def test_get_provider(mock_page):
    providers_found = []
    for filefound in mock_page:
        scrapper = Scrapper(filefound)
        if provider := scrapper.get_providers:
            providers_found.append(provider)
    assert len(providers_found) == 2


def test_get_raw_file(mock_page):
    for filefound in mock_page:
        scrapper = Scrapper(filefound)
        assert isinstance(scrapper.get_raw_file, str)
