from functools import wraps


def _convert(value):
    if value == "0" or value == "0.0":
        final_value = None
        try:
            final_value = int(value)
        except ValueError:
            final_value = float(value)
        finally:
            return final_value if final_value is not None else value
    return value


def convert_second_operand_to_zero_from_string(func_):
    @wraps(func_)
    def wrapper(first_operand, second_operand):
        converted2 = _convert(second_operand)
        return func_(first_operand, converted2)

    return wrapper
