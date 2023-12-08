import pytest
from pathlib import Path
from bs4 import BeautifulSoup
from homedigger.providers.idealista.processor import Idealista
from homedigger.providers.common.schemas.addresses import AddressSchema
from homedigger.providers.common.schemas.contacts import ContactsSchema
from homedigger.providers.idealista.schemas import IdealistaSchema


@pytest.fixture
def mocked_beautiful_soup_page():
    path = Path(__file__).parent
    files_generator = path.rglob("*idealista*.html")
    pagefound = next(files_generator)
    return BeautifulSoup(pagefound.read_text(), "html.parser")


def test_idealista_get_price(mocked_beautiful_soup_page):
    idealista = Idealista(mocked_beautiful_soup_page)
    assert idealista.get_price == 550


def test_idealista_get_bedrooms_number(mocked_beautiful_soup_page):
    idealista = Idealista(mocked_beautiful_soup_page)
    assert idealista.get_bedrooms_number == 2


def test_idealista_get_bathrooms_number(mocked_beautiful_soup_page):
    idealista = Idealista(mocked_beautiful_soup_page)
    assert idealista.get_bathrooms_number == 1


def test_idealista_get_size(mocked_beautiful_soup_page):
    idealista = Idealista(mocked_beautiful_soup_page)
    assert idealista.get_size == 64


def test_idealista_get_floor(mocked_beautiful_soup_page):
    idealista = Idealista(mocked_beautiful_soup_page)
    assert idealista.get_floor == 1


def test_idealista_has_lift(mocked_beautiful_soup_page):
    idealista = Idealista(mocked_beautiful_soup_page)
    assert idealista.has_lift == True


def test_idealista_get_address_dict(mocked_beautiful_soup_page):
    idealista = Idealista(mocked_beautiful_soup_page)
    expected = AddressSchema(
        street="Travesía de Meicende", city="Área de A Coruña, A Coruña"
    )
    assert idealista.get_address_dict == expected


def test_idealista_get_contacts(mocked_beautiful_soup_page):
    idealista = Idealista(mocked_beautiful_soup_page)
    expected = ContactsSchema(name="Metrópoli Servicios", city="A Coruña")
    assert idealista.get_contacts == expected


def test_get_idealista_data(mocked_beautiful_soup_page):
    idealista = Idealista(mocked_beautiful_soup_page)
    expected = IdealistaSchema()
    print(idealista.get_idealista_data)
    assert idealista.get_idealista_data == expected
