from collections import namedtuple, deque

XY = namedtuple("XY", ["x", "y"])

OFFSETS = {
    "<": XY(-1, 0),
    ">": XY(1, 0),
    "^": XY(0, -1),
    "v": XY(0, 1),
}


def part_1_answer(lines):
    warehouse_map, movements = parse(lines)

    robot_pos = find_robot(warehouse_map)

    for movement in movements:

        offset = OFFSETS[movement]

        # Find what's ahead of the robot in the direction of movement
        check = robot_pos
        ahead = []
        while True:
            ahead.append(warehouse_map[check.y][check.x])
            if ahead[-1] == '#':
                break
            check = XY(check.x + offset.x, check.y + offset.y)

        if "." not in ahead[1:]:
            # No empty spaces to move into
            continue

        # Find first empty space in the direction of movement
        empty = XY(robot_pos.x + offset.x, robot_pos.y + offset.y)
        while warehouse_map[empty.y][empty.x] != ".":
            empty = XY(empty.x + offset.x, empty.y + offset.y)

        # Shuffle everything along
        to_pos = empty
        while to_pos != robot_pos:
            from_pos = XY(to_pos.x - offset.x, to_pos.y - offset.y)
            warehouse_map[to_pos.y][to_pos.x] = warehouse_map[from_pos.y][from_pos.x]
            to_pos = from_pos
        warehouse_map[robot_pos.y][robot_pos.x] = "."

        # Update robot position
        robot_pos = XY(robot_pos.x + offset.x, robot_pos.y + offset.y)

    return sum_of_gps_coordinates(warehouse_map)


def find_robot(warehouse_map):
    robot_pos = None
    for y, row in enumerate(warehouse_map):
        for x, cell in enumerate(row):
            if cell == "@":
                robot_pos = XY(x, y)
    return robot_pos


def sum_of_gps_coordinates(warehouse_map):
    total = 0
    for y, row in enumerate(warehouse_map):
        for x, cell in enumerate(row):
            if cell in "O[":
                total += gps_coordinate(x, y)
    return total


def gps_coordinate(x, y):
    return 100 * y + x


def part_2_answer(lines):
    warehouse_map, movements = parse(lines)

    warehouse_map = resize_map(warehouse_map)

    robot_pos = find_robot(warehouse_map)

    for movement in movements:

        offset = OFFSETS[movement]

        cells_to_move = find_adjoining_boxes(warehouse_map, robot_pos, offset)

        # Check cells at the front have empty space in front of them
        if can_move(warehouse_map, cells_to_move, offset):

            # Copy old map
            old_state = [row[::] for row in warehouse_map]

            # Clear old positions
            for pos in cells_to_move:
                warehouse_map[pos.y][pos.x] = "."

            # Populate new positions
            for from_pos in cells_to_move:
                to_pos = XY(from_pos.x + offset.x, from_pos.y + offset.y)
                warehouse_map[to_pos.y][to_pos.x] = old_state[from_pos.y][from_pos.x]

            # Update robot position
            robot_pos = XY(robot_pos.x + offset.x, robot_pos.y + offset.y)

    return sum_of_gps_coordinates(warehouse_map)


def resize_map(warehouse_map):
    for y, old_row in enumerate(warehouse_map):
        warehouse_map[y] = new_row = []
        for cell in old_row:
            if cell == "O":
                new_row.extend("[]")
            elif cell == "@":
                new_row.extend("@.")
            else:
                new_row.extend(cell * 2)
    return warehouse_map


def find_adjoining_boxes(warehouse_map, pos, offset):
    to_visit = deque([pos])
    visited = set()

    while len(to_visit) > 0:

        pos = to_visit.popleft()
        visited.add(pos)

        if warehouse_map[pos.y][pos.x] == "[":
            # Found left half of box - add right half
            right = XY(pos.x + 1, pos.y)
            if right not in visited:
                to_visit.append(right)

        elif warehouse_map[pos.y][pos.x] == "]":
            # Found right half of box - add left half
            left = XY(pos.x - 1, pos.y)
            if left not in visited:
                to_visit.append(left)

        # Add adjacent cell if it's part of a box
        ahead = XY(pos.x + offset.x, pos.y + offset.y)
        if (warehouse_map[ahead.y][ahead.x] in "[]") and (ahead not in visited):
            to_visit.append(ahead)

    return visited


def can_move(warehouse_map, cells_to_move, offset):
    for pos in cells_to_move:
        ahead = XY(pos.x + offset.x, pos.y + offset.y)
        if (warehouse_map[ahead.y][ahead.x] != ".") and (ahead not in cells_to_move):
            return False
    return True


def parse(lines):
    warehouse_map, movements = lines.strip().split("\n\n")
    warehouse_map = [list(row) for row in warehouse_map.split("\n")]
    movements = "".join(movements.split("\n"))
    return warehouse_map, movements
