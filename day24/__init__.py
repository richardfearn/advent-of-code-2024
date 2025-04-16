import operator

import utils

OPERATORS = {
    "AND": operator.and_,
    "OR": operator.or_,
    "XOR": operator.xor,
}

GATE_COLOURS = {
    "AND": "cyan",
    "OR": "red",
    "XOR": "green",
}


class System:

    def __init__(self, lines=None):
        self.wires = set()
        self.values = {}
        self.connections = {}
        self.swapped = set()

        if lines is not None:
            self.parse(lines)

    def parse(self, lines):
        sections = utils.group_lines(lines)
        wire_values = dict(self.parse_wire_value(line) for line in sections[0])
        gates = dict(self.parse_gate(line) for line in sections[1])

        for wire, value in wire_values.items():
            self.add_initial_value(wire, value)

        for output, (input1, op, input2) in gates.items():
            self.add_connection(output, (input1, op, input2))

    @staticmethod
    def parse_wire_value(wire_and_value):
        wire, value = wire_and_value.split(": ")
        return wire, int(value)

    @staticmethod
    def parse_gate(gate_connection):
        input1, op, input2, _, output = gate_connection.split(" ")
        return output, (input1, op, input2)

    def add_initial_value(self, wire, value):
        self.wires.add(wire)
        self.values[wire] = value
        self.connections.pop(wire, None)

    def add_connection(self, output, definition):
        input1, _, input2 = definition
        self.wires.update({input1, input2, output})
        self.connections[output] = definition

    def value(self, wire):
        if wire not in self.values:
            input1, op, input2 = self.connections[wire]
            result = OPERATORS[op](self.value(input1), self.value(input2))
            self.values[wire] = result

        return self.values[wire]

    def copy(self):
        system = System()
        system.wires = self.wires.copy()
        system.values = self.values.copy()
        system.connections = self.connections.copy()
        return system

    def swap(self, a_name, b_name):
        a, b = self.connections[a_name], self.connections[b_name]
        self.connections[a_name], self.connections[b_name] = b, a
        self.swapped.update({a_name, b_name})

    def write_graph(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            print("digraph {{", file=f)
            for output, (input1, op, input2) in self.connections.items():
                print(f"  {output} [fillcolor={GATE_COLOURS[op]},style=filled]", file=f)
                print(f"  {output} -> {input1}", file=f)
                print(f"  {output} -> {input2}", file=f)
            print("}}", file=f)


def part_1_answer(lines):
    system = System(lines)

    digits = "".join(str(system.value(wire))
                     for wire in sorted(system.wires, reverse=True)
                     if wire.startswith("z"))
    return int(digits, 2)
