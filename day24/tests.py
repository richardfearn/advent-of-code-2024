import itertools
import unittest

import day24
import utils

PART_1_EXAMPLE = """
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
"""

PART_1_LARGER_EXAMPLE = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""

PART_2_CARRY_OUT_WIRES = [
    "rdm", "rpn", "qpp", "pvg", "gdb", "scp", "fhc", "rgt",
    "pck", "rnc", "rmd", "crn", "qwd", "rvj", "kvn", "tmp",
    "gvs", "kjh", "rpv", "mwn", "dtm", "ppm", "ftg", "mbg",
    "sjq", "msm", "jrg", "cgr", "whw", "mqt", "bmp", "trb",
    "btb", "wbd", "kwj", "cfp", "dhb", "sdm", "mwg", "mtb",
    "htt", "ckv", "nkh", "rvd"
]


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(4, day24.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_larger_example(self):
        self.assertEqual(2024, day24.part_1_answer(utils.to_lines(PART_1_LARGER_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(43559017878162, day24.part_1_answer(utils.read_input_lines(24)))


class Part2Tests(unittest.TestCase):

    def test_with_input(self):
        system = day24.System(utils.read_input_lines(24))

        system.swap("z06", "fhc")
        system.swap("z11", "qhj")
        system.swap("ggt", "mwh")
        system.swap("hqk", "z35")

        for bit in range(1, 44):
            carry_in_wire = PART_2_CARRY_OUT_WIRES[bit - 1]
            carry_out_wire = PART_2_CARRY_OUT_WIRES[bit]

            with self.subTest(bit=bit, carry_in_wire=carry_in_wire, carry_out_wire=carry_out_wire):
                self.check_full_adder(system, bit, carry_in_wire, carry_out_wire)

        answer = ",".join(sorted(system.swapped))
        self.assertEqual("fhc,ggt,hqk,mwh,qhj,z06,z11,z35", answer)

    def check_full_adder(self, original_system, bit, carry_in_wire, carry_out_wire):
        input_a_wire = wire_name("x", bit)
        input_b_wire = wire_name("y", bit)
        sum_wire = wire_name("z", bit)

        for (input_a, input_b, carry_in) in itertools.product(range(2), repeat=3):
            system = original_system.copy()

            expected_sum = (input_a + input_b + carry_in) & 1
            expected_carry_out = (input_a + input_b + carry_in) >> 1

            system.add_initial_value(input_a_wire, input_a)
            system.add_initial_value(input_b_wire, input_b)
            system.add_initial_value(carry_in_wire, carry_in)

            self.assertEqual(system.value(sum_wire), expected_sum, "sum")
            self.assertEqual(system.value(carry_out_wire), expected_carry_out, "carry")


def wire_name(letter, number):
    return f"{letter}{number:02}"
