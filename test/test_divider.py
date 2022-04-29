import pytest
from src.calculator import divide


def test_divide_int_and_int():
  assert divide(10, 2) == 5

def test_divide_int_and_float():
  assert divide(10, 2.0) == 5.0

def test_divide_zero_and_int():
  assert divide(0, 10) == 0

def test_divide_int_and_zero():
  with pytest.raises(RuntimeError):
    assert divide(10, 0)

def test_divide_int_and_list():
  with pytest.raises(TypeError):
    divide(10, [])

def test_divide_string_and_int():
  with pytest.raises(TypeError):
    divide("lovely", 10)

def test_divide_tuple_and_zero():
  with pytest.raises(TypeError):
    divide((), 0)