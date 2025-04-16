import unittest

import day20
import utils

PART_1_EXAMPLE = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""

PART_1_SAVINGS = {
    2: 14,
    4: 14,
    6: 2,
    8: 4,
    10: 2,
    12: 3,
    20: 1,
    36: 1,
    38: 1,
    40: 1,
    64: 1,
}

PART_2_SAVINGS = {
    50: 32,
    52: 31,
    54: 29,
    56: 39,
    58: 25,
    60: 23,
    62: 20,
    64: 19,
    66: 12,
    68: 14,
    70: 12,
    72: 22,
    74: 4,
    76: 3,
}


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(PART_1_SAVINGS, day20.part_1_savings(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1332, day20.part_1_answer(utils.read_input_lines(20)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(PART_2_SAVINGS, day20.part_2_savings(utils.to_lines(PART_1_EXAMPLE), 50))

    def test_with_input(self):
        self.assertEqual(987695, day20.part_2_answer(utils.read_input_lines(20), 100))
