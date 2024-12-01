import unittest

import day1
import utils

PART_1_EXAMPLE = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(11, day1.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1830467, day1.part_1_answer(utils.read_input_lines(1)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(31, day1.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(26674158, day1.part_2_answer(utils.read_input_lines(1)))
