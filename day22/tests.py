import unittest

import day22
import utils

PART_1_EXAMPLE = """
1
10
100
2024
"""

PART_2_EXAMPLE = """
1
2
3
2024
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(37327623, day22.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(19822877190, day22.part_1_answer(utils.read_input_lines(22)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(23, day22.part_2_answer(utils.to_lines(PART_2_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(2277, day22.part_2_answer(utils.read_input_lines(22)))
