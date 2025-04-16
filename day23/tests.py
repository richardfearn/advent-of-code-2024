import unittest

import day23
import utils

PART_1_EXAMPLE = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(7, day23.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1194, day23.part_1_answer(utils.read_input_lines(23)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual("co,de,ka,ta", day23.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual("bd,bu,dv,gl,qc,rn,so,tm,wf,yl,ys,ze,zr", day23.part_2_answer(utils.read_input_lines(23)))
