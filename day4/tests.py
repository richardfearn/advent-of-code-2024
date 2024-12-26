import unittest

import day4
import utils

PART_1_EXAMPLE = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(18, day4.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(2370, day4.part_1_answer(utils.read_input_lines(4)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(9, day4.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1908, day4.part_2_answer(utils.read_input_lines(4)))
