import pytest
from src.calculator import multiply

def test_multiply_two_integers():
  assert multiply(2, 5) == 10

def test_multiply_int_and_float():
  assert multiply(2, 5.5) == 11

def test_multiply_float_and_float():
  assert multiply(2.0, 5.5) == 11.0

def test_multiply_float_and_zero():
  assert multiply(0, 5.5) == 0

def test_multiply_int_and_list():
  with pytest.raises(TypeError):
    assert multiply(10, [])

def test_multiply_float_and_list():
  with pytest.raises(TypeError):
    assert multiply(10.1, [])

def test_multiply_negative_int_and_float():
  assert multiply(-1, 5.5) == -5.5

def test_multiply_int_and_float_with_string():
  assert multiply("5", "3.0") == 15.0

def test_multiply_int_string_and_zero():
  assert multiply(0, "5") == 0

def test_multiply_int_and_string_conversion():
  with pytest.raises(TypeError):
    assert multiply("5", "asdasdasda")

def test_multiply_int_and_list_conversion():
  with pytest.raises(TypeError):
    assert multiply("5", "[]")