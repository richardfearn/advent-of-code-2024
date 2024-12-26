import unittest

import day7
import utils

PART_1_EXAMPLE = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(3749, day7.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(7885693428401, day7.part_1_answer(utils.read_input_lines(7)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(11387, day7.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(348360680516005, day7.part_2_answer(utils.read_input_lines(7)))
