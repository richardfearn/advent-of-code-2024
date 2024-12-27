import unittest

import day10
import utils

PART_1_EXAMPLE = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(36, day10.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(629, day10.part_1_answer(utils.read_input_lines(10)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(81, day10.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1242, day10.part_2_answer(utils.read_input_lines(10)))
