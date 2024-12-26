import unittest

import day5
import utils

PART_1_EXAMPLE = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(143, day5.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(5064, day5.part_1_answer(utils.read_input_lines(5)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(123, day5.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(5152, day5.part_2_answer(utils.read_input_lines(5)))
