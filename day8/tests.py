import unittest

import day8
import utils

PART_1_EXAMPLE = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(14, day8.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(336, day8.part_1_answer(utils.read_input_lines(8)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(34, day8.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1131, day8.part_2_answer(utils.read_input_lines(8)))
