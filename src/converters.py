from functools import wraps

def _convert(value):
  final_value = None
  if isinstance(value, str):
    try:
      final_value = int(value)
    except ValueError:
      final_value = float(value)
    finally:
      return final_value or value
  return value

def convert_types(func_):
  @wraps(func_)
  def wrapper(number1, number2):
    converted1 = _convert(number1)
    converted2 = _convert(number2)
    return func_(converted1, converted2)

  return wrapper