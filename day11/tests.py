import unittest

import day11
import utils

PART_1_EXAMPLE_2 = """
125 17
"""


class Part1Tests(unittest.TestCase):

    def test_example_2(self):
        self.assertEqual(55312, day11.part_1_answer(utils.to_lines(PART_1_EXAMPLE_2)))

    def test_with_input(self):
        self.assertEqual(183435, day11.part_1_answer(utils.read_input_lines(11)))


class Part2Tests(unittest.TestCase):

    def test_with_input(self):
        self.assertEqual(218279375708592, day11.part_2_answer(utils.read_input_lines(11)))
