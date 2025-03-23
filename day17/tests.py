import unittest

import day17
import utils

PART_1_EXAMPLES = [
    ((None, None, 9), "2,6", (None, 1, None), None),
    ((10, None, None), "5,0,5,1,5,4", (None, None, None), "0,1,2"),
    ((2024, None, None), "0,1,5,4,3,0", (0, None, None), "4,2,5,6,7,7,7,7,3,1,0"),
    ((None, 29, None), "1,7", (None, 26, None), None),
    ((None, 2024, 43690), "4,0", (None, 44354, None), None),
]

PART_1_EXAMPLE_PROGRAM = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

PART_2_EXAMPLE_PROGRAM = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""

REGISTERS = ["A", "B", "C"]


class Part1Tests(unittest.TestCase):

    def test_examples(self):

        for initial_registers, program, expected_registers, expected_outputs in PART_1_EXAMPLES:

            with self.subTest(
                    initial_registers=initial_registers,
                    program=program,
                    expected_registers=expected_registers,
                    expected_outputs=expected_outputs):

                initial_registers = [zero_if_none(n) for n in initial_registers]

                program = [int(n) for n in program.split(",")]

                if expected_outputs is not None:
                    expected_outputs = [int(n) for n in expected_outputs.split(",")]

                actual_registers, actual_outputs = day17.run(initial_registers, program)

                for register, expected, actual in zip(REGISTERS, expected_registers, actual_registers):
                    if expected is not None:
                        self.assertEqual(expected, actual, register)

                if expected_outputs is not None:
                    self.assertEqual(expected_outputs, actual_outputs, "outputs")

    def test_example_program(self):
        self.assertEqual("4,6,3,5,6,3,5,2,1,0", day17.part_1_answer(utils.to_lines(PART_1_EXAMPLE_PROGRAM)))

    def test_with_input(self):
        self.assertEqual("1,0,2,0,5,7,2,1,3", day17.part_1_answer(utils.read_input_lines(17)))


class Part2Tests(unittest.TestCase):

    def test_example_program(self):
        self.part_2_check(utils.to_lines(PART_2_EXAMPLE_PROGRAM), 117440)

    def test_with_input(self):
        answer = day17.part_2_answer(utils.read_input_lines(17))
        self.assertEqual(265652340990875, answer)
        self.part_2_check(utils.read_input_lines(17), answer)

    def part_2_check(self, lines, initial_a_value):
        (a, b, c), program = day17.parse(lines)
        a = initial_a_value
        _, outputs = day17.run((a, b, c), program)
        self.assertEqual(outputs, program)


def zero_if_none(val):
    return val if (val is not None) else 0
