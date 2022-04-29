import pytest
from src.calculator import subtract

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
  with pytest.raises(TypeError):
    assert subtract(10,())

def test_subtract_float_and_list():
  with pytest.raises(TypeError):
    assert subtract(10.0, [])

def test_subtract_float_and_str():
  with pytest.raises(TypeError):
    assert subtract(10.0, "lovely")