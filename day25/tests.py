import unittest

import day25
import utils

PART_1_EXAMPLE = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(3, day25.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(2586, day25.part_1_answer(utils.read_input_lines(25)))
