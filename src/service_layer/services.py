from typing import Union

from src.actions.actions import handle_number_actions
from src.domain.model import allocate
from src.service_layer.converters import convert_second_operand_to_zero_from_string
from src.service_layer.validators import check_second_operand_is_zero


def add(
    first_operand: Union[int, float], second_operand: Union[int, float]
) -> Union[int, float]:
    return handle_number_actions("add", allocate(first_operand, second_operand))()


def subtract(
    first_operand: Union[int, float], second_operand: Union[int, float]
) -> Union[int, float]:
    return handle_number_actions("subtract", allocate(first_operand, second_operand))()


def multiply(
    first_operand: Union[int, float], second_operand: Union[int, float]
) -> Union[int, float]:
    return handle_number_actions("multiply", allocate(first_operand, second_operand))()


@convert_second_operand_to_zero_from_string
@check_second_operand_is_zero
def divide(
    first_operand: Union[int, float], second_operand: Union[int, float]
) -> Union[int, float]:
    return handle_number_actions("divide", allocate(first_operand, second_operand))()
