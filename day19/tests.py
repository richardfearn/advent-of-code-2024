import unittest

import day19
import utils

PART_1_EXAMPLE = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(6, day19.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(342, day19.part_1_answer(utils.read_input_lines(19)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(16, day19.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(891192814474630, day19.part_2_answer(utils.read_input_lines(19)))
