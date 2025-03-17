import unittest

import day18
import utils

PART_1_EXAMPLE = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(22, day18.part_1_answer(utils.to_lines(PART_1_EXAMPLE), 7, 12))

    def test_with_input(self):
        self.assertEqual(334, day18.part_1_answer(utils.read_input_lines(18), 71, 1024))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual("6,1", day18.part_2_answer(utils.to_lines(PART_1_EXAMPLE), 7))

    def test_with_input(self):
        self.assertEqual("20,12", day18.part_2_answer(utils.read_input_lines(18), 1024))
