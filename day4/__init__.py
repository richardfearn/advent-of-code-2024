from enum import Enum, auto
from collections import namedtuple

Position = namedtuple("Position", ["x", "y"])
Size = namedtuple("Size", ["width", "height"])


def part_1_answer(lines):
    size = Size(len(lines[0]), len(lines))
    return sum(count_xmas(lines, size, Position(x, y))
               for x in range(size.width) for y in range(size.height))


def count_xmas(grid, size, pos):
    return sum(1 for direction in Direction if is_xmas(grid, size, pos, direction))


def is_xmas(grid, size, pos, direction):
    word = ""
    dx, dy = direction.offset()
    for i in range(4):
        x = pos.x + i * dx
        y = pos.y + i * dy
        if (0 <= x < size.width) and (0 <= y < size.height):
            word += grid[y][x]
    return word == "XMAS"


def part_2_answer(lines):
    size = Size(len(lines[0]), len(lines))
    return sum(1 for x in range(size.width) for y in range(size.height)
               if is_mas_x(lines, size, Position(x, y)))


def is_mas_x(grid, size, pos):
    x, y = pos
    if (1 <= x < size.width - 1) and (1 <= y < size.height - 1):
        nw_se = grid[y - 1][x - 1] + grid[y][x] + grid[y + 1][x + 1]
        ne_sw = grid[y - 1][x + 1] + grid[y][x] + grid[y + 1][x - 1]
        return all(word in ("MAS", "SAM") for word in (nw_se, ne_sw))
    return False


class Direction(Enum):

    def offset(self):
        return self.value[1]

    NORTH = auto(), (0, -1)
    NORTHEAST = auto(), (1, -1)
    EAST = auto(), (1, 0)
    SOUTHEAST = auto(), (1, 1)
    SOUTH = auto(), (0, 1)
    SOUTHWEST = auto(), (-1, 1)
    WEST = auto(), (-1, 0)
    NORTHWEST = auto(), (-1, -1)
