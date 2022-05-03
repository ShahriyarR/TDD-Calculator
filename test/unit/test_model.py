import pytest

from src.domain.exceptions import UnsupportedModelTypeException
from src.domain.model import Number, allocate


def test_if_number_was_created():
    number = Number(10, 20)
    assert number.first_operand == 10 and number.second_operand == 20


def test_if_two_numbers_are_equal():
    assert Number(10, 20) == Number(10, 20)


def test_number_allocation_int_and_float():
    number = Number(10, 20.5)
    assert allocate(10, 20.5) == number


def test_number_allocation_int_and_int():
    number = Number(10, 20)
    assert allocate(10, 20) == number


def test_number_allocation_int_and_float_string():
    number = Number(34, 45.5)
    assert allocate("34", "45.5") == number


def test_number_allocation_int_and_unsupported_type_conversion():
    with pytest.raises(UnsupportedModelTypeException):
        assert allocate("34", "[]")
