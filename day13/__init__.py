from collections import namedtuple

import numpy as np

import utils

Machine = namedtuple("Machine", ["buttons", "prize"])
Buttons = namedtuple("Buttons", ["a", "b"])
XY = namedtuple("XY", ["x", "y"])

PART_2_OFFSET = 10000000000000


def part_1_answer(lines):
    machines = parse(lines)
    return sum(cost(m) for m in machines)


def part_2_answer(lines):
    machines = parse(lines)
    machines = [adjust(m) for m in machines]
    return sum(cost(m) for m in machines)


def cost(machine):
    (a, b), prize = machine

    coefficients = np.array([[a.x, b.x], [a.y, b.y]])
    values = np.array([prize.x, prize.y])
    solution = np.linalg.solve(coefficients, values)

    a_presses, b_presses = np.round(solution).astype(int)
    pos_x = (a.x * a_presses) + (b.x * b_presses)
    pos_y = (a.y * a_presses) + (b.y * b_presses)

    if (pos_x, pos_y) == prize:
        return (3 * a_presses) + b_presses

    return 0


def adjust(machine):
    return Machine(
        buttons=machine.buttons,
        prize=XY(machine.prize.x + PART_2_OFFSET, machine.prize.y + PART_2_OFFSET))


def parse(lines):
    return [parse_machine(machine) for machine in utils.group_lines(lines)]


def parse_machine(machine):
    a, b = [parse_xy(machine[i]) for i in range(2)]
    prize = parse_xy(machine[2])
    return Machine(buttons=Buttons(a, b), prize=prize)


def parse_xy(line):
    x_y = line.split(": ")[1].split(", ")
    return XY(*(int(n[2:]) for n in x_y))
