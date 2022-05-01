from src.domain.model import allocate
from src.service_layer.validators import check_second_operand_is_zero
from typing import Union

def add(first_operand: Union[int, float], second_operand: Union[int, float]) -> Union[int, float]:
  number = allocate(first_operand, second_operand)
  return number.first_operand + number.second_operand

def subtract(first_operand: Union[int, float], second_operand: Union[int, float]) -> Union[int, float]:
  number = allocate(first_operand, second_operand)
  return number.first_operand - number.second_operand

def multiply(first_operand: Union[int, float], second_operand: Union[int, float]) -> Union[int, float]:
  number = allocate(first_operand, second_operand)
  return number.first_operand * number.second_operand

@check_second_operand_is_zero
def divide(first_operand: Union[int, float], second_operand: Union[int, float]) -> Union[int, float]:
  number = allocate(first_operand, second_operand)
  return number.first_operand / number.second_operand