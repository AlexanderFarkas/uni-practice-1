from calculator import Calculator, Operation
from formatter import format_float
from parser import parse_operator, parse_operand, LocalizedValueError

available_commands = [
    ("help", "Показать справку по командам"),
    ("history", "Показать историю операций"),
    ("clear", "Очистить историю операций"),
    ("exit", "Выйти из программы"),
    ("[число] [оператор] [число]", "Произвести арифметическую операцию. Пример: \"2 + 2\""),
    ("[оператор] [число]", "Произвести арифметическую операцию с последним результатом. Пример: \"+ 2\""),
]


def main():
    calculator = Calculator()
    print_help()
    while True:
        try:
            command = input("Введите команду: ")
            tokens = command.strip().split(" ")
            match tokens:
                case ["history"]:
                    print_history(calculator.history)
                case ["help"]:
                    print_help()
                case ["clear"]:
                    calculator.clear()
                    print("История операций очищена")
                case ["exit"]:
                    print("До свидания!")
                    exit(0)
                case [operator, right_operand]:
                    result = calculator.calculate(
                        operator=parse_operator(operator),
                        right_operand=parse_operand(right_operand),
                    )
                    print_result(result)

                case [left_operand, operator, right_operand]:
                    result = calculator.calculate(
                        left_operand=parse_operand(left_operand),
                        operator=parse_operator(operator),
                        right_operand=parse_operand(right_operand),
                    )
                    print_result(result)
                case _:
                    print("Неверная команда")

        except LocalizedValueError as e:
            print(e)
        except ZeroDivisionError:
            print("Деление на ноль запрещено")
        except Exception as e:
            print("Непредвиденная ошибка: ", e)

        print()  # new line


def print_history(history: list[Operation]):
    if len(history) == 0:
        print("История операций пуста")
        return

    for operation in history:
        print(operation)


def print_help():
    for command, description in available_commands:
        print(f"{command}: {description}")


def print_result(result: float):
    print(f"Результат: {format_float(result)}")


if __name__ == '__main__':
    main()
