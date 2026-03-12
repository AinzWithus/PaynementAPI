import pytest
from utils.validators import validate_amount, validate_currency


def test_amount_valid():
    assert validate_amount(100) == True


def test_amount_zero():
    with pytest.raises(ValueError):
        validate_amount(0)


def test_amount_negative():
    with pytest.raises(ValueError):
        validate_amount(-10)


def test_amount_decimal():
    with pytest.raises(ValueError):
        validate_amount(10.5)


def test_currency_valid():
    assert validate_currency("USD") == True


def test_currency_invalid():
    with pytest.raises(ValueError):
        validate_currency("US")