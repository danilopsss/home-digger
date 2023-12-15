import re

from typing import Union
from homedigger.core.utils.logging import log_this
from homedigger.core.abstract.sanitization import SanitizationABC
from homedigger.providers.common.types.providers import Provider


class Sanitization(SanitizationABC):

    @staticmethod
    @log_this
    def clean_up_integer(value: Union[str, int]) -> int:
        converted_value = re.sub(r"[\D\Wa-zA-Z]", "", str(value))
        if converted_value:
            return int(converted_value)
        return 0

    @staticmethod
    @log_this
    def clean_up_text(value: str) -> str:
        clean_patterns = ((r"[\t\n\r]", ""), (r"\s{2,}", ""))
        for pattern, replacement in clean_patterns:
            value = re.sub(pattern, replacement, value)
        return value

    @staticmethod
    @log_this
    def clean_up_by_schema(data: dict, model: Provider) -> Provider:
        model = model.model_json_schema()
        for key in model.get("properties"):
            if key in data:
                data_type = model.get("properties").get(key).get("type")
                value = data.get(key)
                if not type(value) == data_type:
                    data[key] = Sanitization.clean_up_integer(value)
                if data_type == data_type:
                    data[key] = Sanitization.clean_up_text(value)
        return Provider(**data)
