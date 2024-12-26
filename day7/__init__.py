import operator
from collections import namedtuple

Equation = namedtuple("Equation", ["test_value", "numbers"])


def concat(a, b):
    return int(str(a) + str(b))


PART_1_OPERATORS = [operator.mul, operator.add]
PART_2_OPERATORS = PART_1_OPERATORS + [concat]


def part_1_answer(lines):
    equations = parse(lines)
    return sum(e.test_value for e in equations if is_possible(PART_1_OPERATORS, e))


def part_2_answer(lines):
    equations = parse(lines)
    return sum(e.test_value for e in equations if is_possible(PART_2_OPERATORS, e))


def is_possible(operators, equation):
    return dfs(operators, equation, equation.numbers[0], 1)


def dfs(operators, equation, value_so_far, next_number):
    if value_so_far > equation.test_value:
        return False

    if next_number == len(equation.numbers):
        return value_so_far == equation.test_value

    return any(dfs(operators, equation, op(value_so_far, equation.numbers[next_number]), next_number + 1)
               for op in operators)


def parse(lines):
    return [parse_equation(line) for line in lines]


def parse_equation(line):
    test_value, numbers = line.split(": ")
    test_value = int(test_value)
    numbers = [int(n) for n in numbers.split(" ")]
    return Equation(test_value, numbers)
