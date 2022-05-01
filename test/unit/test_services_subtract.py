import pytest
from src.service_layer.services import subtract
from src.domain.exceptions import UnsupportedModelTypeException

def test_subtract_two_integers():
  assert subtract(10, 4) == 6

def test_subtract_int_and_float():
  assert subtract(10, 5.5) == 4.5

def test_subtract_zero_and_int():
  assert subtract(0, 10) == -10

def test_subtract_negative_int_and_int():
  assert subtract(-5, 10) == -15

def test_subtract_negative_int_and_float():
  assert subtract(-5, 10.5) == -15.5

def test_subtract_int_and_tuple():
  with pytest.raises(UnsupportedModelTypeException):
    assert subtract(10,())

def test_subtract_float_and_list():
  with pytest.raises(UnsupportedModelTypeException):
    assert subtract(10.0, [])

def test_subtract_float_and_str():
  with pytest.raises(UnsupportedModelTypeException):
    assert subtract(10.0, "lovely")

def test_subtract_int_and_float_with_string():
  assert subtract("5", "3.0") == 2.0

def test_subtract_int_string_and_zero():
  assert subtract(0, "5") == -5

def test_subtract_int_and_string_conversion():
  with pytest.raises(UnsupportedModelTypeException):
    assert subtract("5", "asdasdasda")

def test_subtract_int_and_list_conversion():
  with pytest.raises(UnsupportedModelTypeException):
    assert subtract("5", "[]")