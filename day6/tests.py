import unittest

import day6
import utils

PART_1_EXAMPLE = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(41, day6.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(4903, day6.part_1_answer(utils.read_input_lines(6)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(6, day6.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1911, day6.part_2_answer(utils.read_input_lines(6)))
