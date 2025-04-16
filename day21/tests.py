import unittest

import day21
import utils

PART_1_EXAMPLE = """
029A
980A
179A
456A
379A
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(126384, day21.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(163920, day21.part_1_answer(utils.read_input_lines(21)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(154115708116294, day21.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(204040805018350, day21.part_2_answer(utils.read_input_lines(21)))
