import unittest

import day14
import utils

PART_1_EXAMPLE = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(12, day14.part_1_answer(utils.to_lines(PART_1_EXAMPLE), 11, 7, 100))

    def test_with_input(self):
        self.assertEqual(218433348, day14.part_1_answer(utils.read_input_lines(14), 101, 103, 100))


class Part2Tests(unittest.TestCase):

    def test_with_input(self):
        self.assertEqual(6512, day14.part_2_answer(utils.read_input_lines(14), 101, 103))
