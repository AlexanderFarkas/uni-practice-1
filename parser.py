from calculator import Operator
from localized_value_error import LocalizedValueError


def parse_operand(value: str) -> float:
    try:
        return float(value.strip())
    except ValueError:
        raise LocalizedValueError("Неверный операнд")


def parse_operator(operator: str) -> Operator:
    operator = operator.strip()
    if operator not in ["+", "-", "*", "/"]:
        raise LocalizedValueError("Неверный оператор")

    return operator
