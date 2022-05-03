from functools import wraps
from src.service_layer.exceptions import ServiceAttemptZeroDivisionException

def check_second_operand_is_zero(func_):
  @wraps(func_)
  def wrapper(first_operand, second_operand):
    if second_operand == 0:
      raise ServiceAttemptZeroDivisionException("Division by zero prohibited!")
    return func_(first_operand, second_operand)
  return wrapper