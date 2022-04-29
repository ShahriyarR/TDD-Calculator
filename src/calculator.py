from .validators import check_supported_operand_types

@check_supported_operand_types
def add(number1, number2):
    return number1 + number2

@check_supported_operand_types
def subtract(number1, number2):
  return number1 - number2

@check_supported_operand_types
def multiply(number1, number2):
  return number1 * number2