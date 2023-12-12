import re
import pytest

from homedigger.core.utils.cleanup import Sanitization


@pytest.fixture
def not_clean_values():
    return [
        "€ 1234 \n",
        "1234,\n",
        "Value Of 1234.56\n",
        "1234.   56,\n",
        "1234.56.78\n",
        "1234.56.78,\n",
        "1234.56.78.90\n",
        "1234.56.78.90,\n",
        "       1234.\n\t\r",
        "1234., € \n\t\r ",
    ]


@pytest.fixture
def prohibited_charaters():
    return re.compile(r"([\n\t\r]|\s{2,})")


@pytest.fixture
def not_clean_text():
    return [
        "Lorem ipsum \rdolor sit amet, consectetur  \t\tadipiscing elit.\n",
        "Sed ut\tperspiciatis unde omnis iste natus error   sit voluptatem.\n",
        "At vero eos et accusamus et iusto odio dignissimos ducimus.\n",
        "Nam libero tempore,   cum soluta nobis est eligendi optio cumque.\n",
        "Temporibus autem quibusdam et aut officiis   debitis aut rerum.\n",
        "Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut.\n",
        "Ut enim ad\tminima veniam,   quis nostrum exercitationem ullam corporis.\n",
        "Quis autem vel eum iure reprehenderit qui in ea voluptate.\n",
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa.\n",
        "Duis aute irure\r\rdolor in reprehenderit in voluptate velit esse.\n",
    ]


def test_clean_up_integer(not_clean_values, prohibited_charaters):
    for value in not_clean_values:
        result = Sanitization.clean_up_integer(value)
        assert not re.findall(prohibited_charaters, str(result))
        assert isinstance(result, int)


def test_clean_up_text(not_clean_text, prohibited_charaters):
    for value in not_clean_text:
        result = Sanitization.clean_up_text(value)
        assert not re.findall(prohibited_charaters, result)
