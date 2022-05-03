from src.domain.model import Number


def handle_number_actions(action_name: str, number: Number) -> callable:
    return {
        "add": lambda: number.first_operand + number.second_operand,
        "subtract": lambda: number.first_operand - number.second_operand,
        "multiply": lambda: number.first_operand * number.second_operand,
        "divide": lambda: number.first_operand / number.second_operand,
    }[action_name]
