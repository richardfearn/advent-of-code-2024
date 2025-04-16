import itertools

import utils

FULL_ROW = "#####"


def part_1_answer(lines):
    locks, keys = parse(lines)
    return sum(1 for (lock, key) in itertools.product(locks, keys) if lock_and_key_fit_together(lock, key))


def lock_and_key_fit_together(lock, key):
    return all((lock[i] + key[i]) <= 5 for i in range(5))


def parse(lines):
    schematics = utils.group_lines(lines)

    locks = []
    keys = []

    for schematic in schematics:
        if schematic[0] == FULL_ROW:
            locks.append(parse_schematic(schematic[1:-1]))
        elif schematic[-1] == FULL_ROW:
            keys.append(parse_schematic(schematic[-2:0:-1]))

    return locks, keys


def parse_schematic(lines):
    columns = zip(*lines)
    return tuple(column.count("#") for column in columns)
