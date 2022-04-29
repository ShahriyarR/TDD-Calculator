from functools import wraps


def check_supported_operand_types(func_):
    @wraps(func_)
    def wrapper(number1, number2):
        if not (isinstance(number1, int) or isinstance(number1, float)):
            raise TypeError("Unsupported operand type")

        if not (isinstance(number2, int) or isinstance(number2, float)):
            raise TypeError("Unsupported operand type")

        return func_(number1, number2)

    return wrapper

def check_second_operand_is_zero(func_):
  @wraps(func_)
  def wrapper(number1, number2):
    if number2 == 0:
      raise RuntimeError("Division by zero is not supported!")
    return func_(number1, number2)
  return wrapper