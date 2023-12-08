import re
from bs4 import BeautifulSoup
from collections import namedtuple
from homedigger.core.abstract.providers import ProvidersInformationABC
from homedigger.providers.common.cleanup import Sanitization
from homedigger.providers.common.schemas.addresses import AddressSchema
from homedigger.providers.common.schemas.contacts import ContactsSchema
from homedigger.providers.idealista.schemas import IdealistaSchema


class Idealista(ProvidersInformationABC):
    def __init__(self, parsed_html: BeautifulSoup):
        self._soup = parsed_html
        self._rules = namedtuple("Rules", ["search_method", "query"])

    @property
    def _scrapper_rules(self):
        return {
            "price": self._rules("select", "span.info-data-price"),
            "location": self._rules("select", "h2.ide-box-detail-h2 + ul"),
            "contact": self._rules("select", "a.about-advertiser-name"),
            "general_info": self._rules(
                "select", "div.details-property_features > ul:last-child"
            ),
        }

    @property
    def _extraction_patterns(self):
        return {
            "bedrooms": r"\d{,3}(?=\shabitac)",
            "bathrooms": r"\d{,3}(?=\sbaño)",
            "size": r"\d{,3}(?=\sm²)",
            "lift": r"\w{3}(?=\sascensor)",
            "floor": r"(bajo|\d{,2}.)(?=\s(interior|exterior))",
        }

    @property
    def get_soup(self) -> str:
        return self._soup

    @property
    def _get_details(self):
        general_rules = self._scrapper_rules["general_info"]
        return getattr(self._soup, general_rules.search_method)(general_rules.query)

    @property
    def get_price(self) -> int:
        price_rules = self._scrapper_rules["price"]
        price = getattr(self._soup, price_rules.search_method)(price_rules.query)[0]
        return Sanitization.clean_up_integer(price.text)

    @property
    def get_size(self) -> int:
        pattern = self._extraction_patterns["size"]
        size = self.extract_by_pattern(pattern=pattern, text=self._get_details[0].text)
        return Sanitization.clean_up_integer(size)

    @property
    def get_bathrooms_number(self):
        pattern = self._extraction_patterns["bathrooms"]
        bathroom = self.extract_by_pattern(
            pattern=pattern, text=self._get_details[0].text
        )
        return Sanitization.clean_up_integer(bathroom)

    @property
    def get_bedrooms_number(self):
        pattern = self._extraction_patterns["bedrooms"]
        bedroom = self.extract_by_pattern(
            pattern=pattern, text=self._get_details[0].text
        )
        return Sanitization.clean_up_integer(bedroom)

    @property
    def has_lift(self):
        pattern = self._extraction_patterns["lift"]
        lift = self.extract_by_pattern(pattern=pattern, text=self._get_details[1].text)
        return lift.lower() == "con"

    @property
    def get_floor(self):
        pattern = self._extraction_patterns["floor"]
        floor = self.extract_by_pattern(pattern=pattern, text=self._get_details[1].text)
        return Sanitization.clean_up_integer(floor)

    @property
    def get_address_dict(self):
        location_rules = self._scrapper_rules["location"]
        location = getattr(self._soup, location_rules.search_method)(
            location_rules.query
        )[0]
        street = location.select("li:first-child")[0].text
        city = location.select("li:last-child")[0].text

        return AddressSchema(
            street=Sanitization.clean_up_text(street),
            city=Sanitization.clean_up_text(city),
        )

    @property
    def get_contacts(self):
        contact_rules = self._scrapper_rules["contact"]
        contact = getattr(self._soup, contact_rules.search_method)(contact_rules.query)
        if contact:
            contact = contact[0]

        city = getattr(self._soup, contact_rules.search_method)(
            contact_rules.query + " + span"
        )
        if city:
            city = city[0]

        return ContactsSchema(
            name=Sanitization.clean_up_text(getattr(contact, "text", "")),
            city=Sanitization.clean_up_text(getattr(city, "text", "")),
        )

    @property
    def get_data(self):
        return IdealistaSchema(
            price=self.get_price,
            size=self.get_size,
            bathrooms=self.get_bathrooms_number,
            bedrooms=self.get_bedrooms_number,
            has_lift=self.has_lift,
            floor=self.get_floor,
            address=self.get_address_dict,
            contact=self.get_contacts,
        )

    def extract_by_pattern(self, *, pattern: str, text: str) -> str:
        if found := re.findall(pattern, text, flags=re.IGNORECASE):
            return found[0]
        return ""
