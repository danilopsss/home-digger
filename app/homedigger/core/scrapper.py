from bs4 import BeautifulSoup
from homedigger.core.utils.logging import log_this
from homedigger.core.abstract.scrapper import ScrapperABC
from homedigger.providers.register import PROVIDERS_REGISTER
from homedigger.providers.idealista.processor import Idealista
from homedigger.providers.common.types.providers import Provider


class Scrapper(ScrapperABC):
    def __init__(self, filepath: str):
        self._html = open(filepath, "r").read()
        self._soup = BeautifulSoup(self._html, "html.parser")
        self._providers = {"idealista": Idealista}

    @property
    @log_this
    def get_raw_file(self) -> str:
        return self._html.replace("\n", "")

    @property
    @log_this
    def get_providers(self) -> dict[str, Provider]:
        for provider in PROVIDERS_REGISTER:
            if provider in self.get_raw_file:
                return provider

    @log_this
    def run(self) -> Provider:
        provider = self._providers[self.get_providers](self._soup)
        return provider.get_data
