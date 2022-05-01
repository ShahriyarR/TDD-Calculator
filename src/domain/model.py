from dataclasses import dataclass
from typing import Union
from src.domain.converters import convert_model_types
from src.domain.validators import check_supported_model_types

@dataclass(frozen=True)
class Number:
  first_operand: Union[int, float]
  second_operand: Union[int, float]

@convert_model_types
@check_supported_model_types
def allocate(first_operand: Union[int, float],
  second_operand: Union[int, float]) -> Number:
    return Number(first_operand, second_operand)