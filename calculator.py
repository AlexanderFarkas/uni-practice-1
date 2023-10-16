from dataclasses import dataclass, field
from typing import Literal, Optional

from formatter import format_float
from localized_value_error import LocalizedValueError


class Calculator:
    def __init__(self):
        self.history: list[Operation] = []

    def calculate(self, *, operator: 'Operator', right_operand: float, left_operand: Optional[float] = None, ) -> float:
        result: float

        if left_operand is None:
            left_operand = self.__get_last_result()

        operation = Operation(
            left_operand=left_operand,
            right_operand=right_operand,
            operator=operator,
        )

        self.history.append(operation)
        return operation.result

    def clear(self):
        self.history = []

    def __get_last_result(self):
        if len(self.history) == 0:
            raise LocalizedValueError(
                "История операций пуста"
            )

        return self.history[-1].result


Operator = Literal["+", "-", "*", "/"]


@dataclass
class Operation:
    left_operand: float
    right_operand: float
    operator: Operator
    result: float = field(init=False)

    def __post_init__(self):
        self.result = self.__calculate_result()

    def __str__(self):
        return f"{format_float(self.left_operand)} {self.operator} {format_float(self.right_operand)} = {format_float(self.result)}"

    def __calculate_result(self):
        match self.operator:
            case "+":
                return self.left_operand + self.right_operand
            case "-":
                return self.left_operand - self.right_operand
            case "*":
                return self.left_operand * self.right_operand
            case "/":
                return self.left_operand / self.right_operand
            case _:
                raise LocalizedValueError("Неверный оператор")
