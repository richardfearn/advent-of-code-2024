import unittest

import day9
import utils

PART_1_EXAMPLE = """
2333133121414131402
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(1928, day9.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(6415184586041, day9.part_1_answer(utils.read_input_lines(9)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(2858, day9.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(6436819084274, day9.part_2_answer(utils.read_input_lines(9)))
