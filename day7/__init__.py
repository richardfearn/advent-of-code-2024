import itertools
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
    num_operators_needed = len(equation.numbers) - 1
    return any(is_correct(equation, ops)
               for ops in itertools.product(operators, repeat=num_operators_needed))


def is_correct(equation, ops):
    total = equation.numbers[0]
    for op, num in zip(ops, equation.numbers[1:]):
        total = op(total, num)
        if total > equation.test_value:
            return False
    return total == equation.test_value


def parse(lines):
    return [parse_equation(line) for line in lines]


def parse_equation(line):
    test_value, numbers = line.split(": ")
    test_value = int(test_value)
    numbers = [int(n) for n in numbers.split(" ")]
    return Equation(test_value, numbers)
