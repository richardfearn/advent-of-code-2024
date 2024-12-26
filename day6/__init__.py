from collections import namedtuple
from enum import Enum, auto

Offset = namedtuple("Offset", ["x", "y"])
Size = namedtuple("Size", ["width", "height"])


def part_1_answer(lines):
    grid, size, start_pos = parse(lines)
    return len(visited_positions(grid, size, start_pos))


def visited_positions(grid, size, start_pos):
    px, py = p = start_pos
    direction = Direction.NORTH
    visited = {p}

    while True:
        nx, ny = n = (px + direction.offset().x), (py + direction.offset().y)

        if is_outside_grid(n, size):
            break

        if grid[ny][nx] == "#":
            direction = TURN[direction]
        else:
            px, py = p = n
            visited.add(p)

    return visited


def part_2_answer(lines):
    grid, size, start_pos = parse(lines)
    candidates = visited_positions(grid, size, start_pos) - {start_pos}

    return sum(1 for candidate in candidates
               if will_loop(grid, size, start_pos, candidate))


def will_loop(grid, size, start_pos, obstacle_pos):
    px, py = p = start_pos
    direction = Direction.NORTH
    visited = {(direction, p)}

    while True:
        nx, ny = n = (px + direction.offset().x), (py + direction.offset().y)

        if is_outside_grid(n, size):
            break

        if (n == obstacle_pos) or (grid[ny][nx] == "#"):
            direction = TURN[direction]
        else:
            px, py = p = n
            new_state = (direction, p)
            if new_state in visited:
                return True
            visited.add(new_state)

    return False


def is_outside_grid(pos, size):
    x, y = pos
    return (x < 0) or (x == size.width) or (y < 0) or (y == size.height)


def parse(lines):
    sx = sy = None
    width, height = len(lines[0]), len(lines)
    grid = [list(line) for line in lines]

    for y, row in enumerate(grid):
        if "^" in row:
            sx, sy = row.index("^"), y
            break
    grid[sy][sx] = "."

    return grid, Size(width, height), (sx, sy)


class Direction(Enum):

    def offset(self):
        return self.value[1]

    NORTH = auto(), Offset(0, -1)
    EAST = auto(), Offset(1, 0)
    SOUTH = auto(), Offset(0, 1)
    WEST = auto(), Offset(-1, 0)


TURN = {
    Direction.NORTH: Direction.EAST,
    Direction.EAST: Direction.SOUTH,
    Direction.SOUTH: Direction.WEST,
    Direction.WEST: Direction.NORTH,
}
