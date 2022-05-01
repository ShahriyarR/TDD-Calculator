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

def convert_model_types(func_):
  @wraps(func_)
  def wrapper(first_operand, second_operand):
    converted1 = _convert(first_operand)
    converted2 = _convert(second_operand)
    return func_(converted1, converted2)

  return wrapper