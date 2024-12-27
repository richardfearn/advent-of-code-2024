import unittest

import day13
import utils

PART_1_EXAMPLE = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(480, day13.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(34787, day13.part_1_answer(utils.read_input_lines(13)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(875318608908, day13.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(85644161121698, day13.part_2_answer(utils.read_input_lines(13)))
