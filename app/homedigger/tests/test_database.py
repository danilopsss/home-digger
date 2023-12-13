import pytest
from unittest.mock import patch
from pydantic import ValidationError
from homedigger.providers.common.schemas.addresses import AddressSchema
from homedigger.providers.common.schemas.contacts import ContactsSchema
from homedigger.providers.idealista.schemas import IdealistaSchema


@pytest.fixture
def mocked_contact():
    return ContactsSchema(
            name='Metrópoli Servicios',
            city='A Coruña'
        )

@pytest.fixture
def mocked_address():
    return AddressSchema(
            street="Travesía de Meicende",
            city="Área de A Coruña, A Coruña"
        )

@pytest.fixture
def mocked_idealista(mocked_contact, mocked_address):
    return IdealistaSchema(
        price=550,
        size=64,
        bathrooms=1,
        bedrooms=2,
        has_lift=True,
        floor=1,
        link='https://www.idealista.com/inmueble/103375656/',
        address=mocked_address,
        contact=mocked_contact
    )

@patch("sqlalchemy.orm.session.Session.add")
@patch("sqlalchemy.orm.session.Session.commit")
def test_save_model_to_db(add, commit, mocked_idealista):
    result = mocked_idealista.save()
    assert add.call_count == 1
    assert commit.call_count == 1

    try:
        IdealistaSchema.model_validate(result)
    except ValidationError:
        pytest.fail("Shouldn't raise ValidationError")
