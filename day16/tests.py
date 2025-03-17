import unittest

import day16
import utils

PART_1_EXAMPLE_1 = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

PART_1_EXAMPLE_2 = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""


class Part1Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(7036, day16.part_1_answer(utils.to_lines(PART_1_EXAMPLE_1)))

    def test_example_2(self):
        self.assertEqual(11048, day16.part_1_answer(utils.to_lines(PART_1_EXAMPLE_2)))

    def test_with_input(self):
        self.assertEqual(105508, day16.part_1_answer(utils.read_input_lines(16)))


class Part2Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(45, day16.part_2_answer(utils.to_lines(PART_1_EXAMPLE_1)))

    def test_example_2(self):
        self.assertEqual(64, day16.part_2_answer(utils.to_lines(PART_1_EXAMPLE_2)))

    def test_with_input(self):
        self.assertEqual(548, day16.part_2_answer(utils.read_input_lines(16)))
