import unittest

import day3
import utils

PART_1_EXAMPLE = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(161, day3.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(178538786, day3.part_1_answer(utils.read_input_lines(3)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(48, day3.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(102467299, day3.part_2_answer(utils.read_input_lines(3)))
