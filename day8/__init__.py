import collections
import itertools


def part_1_answer(lines):
    size, antennas = parse(lines)

    anti_nodes = set()
    for positions in antennas.values():
        for pos1, pos2 in itertools.combinations(positions, 2):
            offset = (pos2[0] - pos1[0], pos2[1] - pos1[1])
            first = (pos1[0] - offset[0], pos1[1] - offset[1])
            second = (pos2[0] + offset[0], pos2[1] + offset[1])
            add_anti_node_if_in_grid(anti_nodes, size, first)
            add_anti_node_if_in_grid(anti_nodes, size, second)
    return len(anti_nodes)


def add_anti_node_if_in_grid(anti_nodes, size, pos):
    if is_in_grid(size, pos):
        anti_nodes.add(pos)


def is_in_grid(size, pos):
    width, height = size
    return (0 <= pos[0] < width) and (0 <= pos[1] < height)


def part_2_answer(lines):
    size, antennas = parse(lines)

    anti_nodes = set()
    for positions in antennas.values():
        for pos1, pos2 in itertools.combinations(positions, 2):
            offset1 = (pos2[0] - pos1[0], pos2[1] - pos1[1])
            offset2 = (-offset1[0], -offset1[1])
            add_anti_nodes(anti_nodes, size, pos1, offset1)
            add_anti_nodes(anti_nodes, size, pos2, offset2)
    return len(anti_nodes)


def add_anti_nodes(anti_nodes, size, pos, offset):
    while is_in_grid(size, pos):
        anti_nodes.add(pos)
        pos = (pos[0] + offset[0], pos[1] + offset[1])


def parse(lines):
    width, height = len(lines[0]), len(lines)
    positions = collections.defaultdict(list)
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell != '.':
                positions[cell].append((x, y))
    return (width, height), positions
