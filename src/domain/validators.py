from functools import wraps

from src.domain.exceptions import UnsupportedModelTypeException


def check_supported_model_types(func_):
    @wraps(func_)
    def wrapper(first_operand, second_operand):
        if not (isinstance(first_operand, int) or isinstance(first_operand, float)):
            raise UnsupportedModelTypeException(
                "Unsupported type: use int and float instead"
            )

        if not (isinstance(second_operand, int) or isinstance(second_operand, float)):
            raise UnsupportedModelTypeException(
                "Unsupported type: use int and float instead"
            )

        return func_(first_operand, second_operand)

    return wrapper
