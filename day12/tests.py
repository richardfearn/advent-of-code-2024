import unittest

import day12
import utils

PART_1_EXAMPLE_1 = """
AAAA
BBCD
BBCC
EEEC
"""

PART_1_EXAMPLE_2 = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""

PART_1_EXAMPLE_3 = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

PART_2_EXAMPLE_3 = """
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
"""

PART_2_EXAMPLE_4 = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
"""


class Part1Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(140, day12.part_1_answer(utils.to_lines(PART_1_EXAMPLE_1)))

    def test_example_2(self):
        self.assertEqual(772, day12.part_1_answer(utils.to_lines(PART_1_EXAMPLE_2)))

    def test_example_3(self):
        self.assertEqual(1930, day12.part_1_answer(utils.to_lines(PART_1_EXAMPLE_3)))

    def test_with_input(self):
        self.assertEqual(1396298, day12.part_1_answer(utils.read_input_lines(12)))


class Part2Tests(unittest.TestCase):

    def test_part_1_example_1(self):
        self.assertEqual(80, day12.part_2_answer(utils.to_lines(PART_1_EXAMPLE_1)))

    def test_part_1_example_2(self):
        self.assertEqual(436, day12.part_2_answer(utils.to_lines(PART_1_EXAMPLE_2)))

    def test_part_2_example_3(self):
        self.assertEqual(236, day12.part_2_answer(utils.to_lines(PART_2_EXAMPLE_3)))

    def test_part_2_example_4(self):
        self.assertEqual(368, day12.part_2_answer(utils.to_lines(PART_2_EXAMPLE_4)))

    def test_part_1_example_3(self):
        self.assertEqual(1206, day12.part_2_answer(utils.to_lines(PART_1_EXAMPLE_3)))

    def test_with_input(self):
        self.assertEqual(853588, day12.part_2_answer(utils.read_input_lines(12)))
