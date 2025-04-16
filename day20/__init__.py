from collections import defaultdict, namedtuple

XY = namedtuple("XY", ["x", "y"])

UP, DOWN, LEFT, RIGHT = XY(0, -1), XY(0, 1), XY(-1, 0), XY(1, 0)


def add(p, o):
    return XY(p.x + o.x, p.y + o.y)


class Grid:
    # pylint: disable=too-few-public-methods

    def __init__(self, lines):
        self.grid = [list(line) for line in lines]
        self.size = XY(len(self.grid[0]), len(self.grid))
        self.start = self.end = self.path = None

        self._find_start_and_end()
        self._find_path()

    def _find_start_and_end(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                pos = XY(x, y)
                if cell in "SE":
                    if cell == "S":
                        self.start = pos
                    elif cell == "E":
                        self.end = pos
                    self.grid[y][x] = "."

    def _find_path(self):
        pos = self.start
        self.path = [pos]
        visited = {pos}

        while pos != self.end:
            for offset in (UP, DOWN, LEFT, RIGHT):
                neighbour = add(pos, offset)
                if (self.cell(neighbour) == ".") and (neighbour not in visited):
                    self.path.append(neighbour)
                    visited.add(neighbour)
                    pos = neighbour

    def cell(self, pos):
        return self.grid[pos.y][pos.x]


def part_1_answer(lines):
    savings = part_1_savings(lines)
    return sum(count for (saving, count) in savings.items() if saving >= 100)


def part_1_savings(lines):
    grid = Grid(lines)
    path_pos_indices = {pos: index for (index, pos) in enumerate(grid.path)}

    savings = defaultdict(int)

    for possible_cheat in find_possible_part_1_cheats(grid):
        cheat_start, cheat_end = possible_cheat
        start_index = path_pos_indices[cheat_start]
        end_index = path_pos_indices[cheat_end]
        saving = abs(end_index - start_index) - 2
        savings[saving] += 1

    return dict(savings)


def find_possible_part_1_cheats(grid):
    for y in range(1, grid.size.y - 1):
        for x in range(1, grid.size.x - 1):
            pos = XY(x, y)
            if grid.cell(pos) == "#":

                above, below = add(pos, UP), add(pos, DOWN)
                if (grid.cell(above) == ".") and (grid.cell(below) == "."):
                    yield above, below

                left, right = add(pos, LEFT), add(pos, RIGHT)
                if (grid.cell(left) == ".") and (grid.cell(right) == "."):
                    yield left, right


def part_2_answer(lines, min_saving):
    savings = part_2_savings(lines, min_saving)
    return sum(savings.values())


def part_2_savings(lines, min_saving):
    grid = Grid(lines)

    savings = defaultdict(int)

    for i, p1 in enumerate(grid.path):
        for j in range(i + 1, len(grid.path)):
            p2 = grid.path[j]
            full_distance = j - i
            if full_distance >= min_saving:
                manhattan_dist = manhattan_distance(p1, p2)
                if manhattan_dist <= 20:
                    saving = full_distance - manhattan_dist
                    if saving >= min_saving:
                        savings[saving] += 1

    return dict(savings)


def manhattan_distance(p1, p2):
    return abs(p2.x - p1.x) + abs(p2.y - p1.y)
