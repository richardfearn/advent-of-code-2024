import unittest

import day2
import utils

PART_1_EXAMPLE = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(2, day2.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(421, day2.part_1_answer(utils.read_input_lines(2)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(4, day2.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(476, day2.part_2_answer(utils.read_input_lines(2)))
