from functools import wraps

def check_second_operand_is_zero(func_):
  @wraps(func_)
  def wrapper(number1, number2):
    if number2 == 0:
      raise RuntimeError("Division by zero is not supported!")
    return func_(number1, number2)
  return wrapper