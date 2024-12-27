from collections import namedtuple

Size = namedtuple("Size", ["width", "height"])
Position = namedtuple("Position", ["x", "y"])
Offset = namedtuple("Offset", ["x", "y"])

UP, DOWN, LEFT, RIGHT = Offset(0, -1), Offset(0, 1), Offset(-1, 0), Offset(1, 0)


def part_1_answer(lines):
    grid, size = parse(lines)

    return sum(trailhead_score(grid, size, Position(x, y))
               for y, row in enumerate(grid)
               for x, cell in enumerate(row)
               if cell == 0)


def trailhead_score(grid, size, trailhead):
    visited = set()
    nine_height_positions = set()
    score_search(grid, size, visited, nine_height_positions, trailhead)
    return len(nine_height_positions)


def score_search(grid, size, visited, nine_height_positions, pos):
    visited.add(pos)
    current_height = grid[pos.y][pos.x]

    if current_height == 9:
        nine_height_positions.add(pos)

    for offset in UP, DOWN, LEFT, RIGHT:
        new_pos = Position(pos.x + offset.x, pos.y + offset.y)
        if (0 <= new_pos.x < size.width) and (0 <= new_pos.y < size.height):
            new_height = grid[new_pos.y][new_pos.x]
            if new_height == (current_height + 1):
                if new_pos not in visited:
                    score_search(grid, size, visited, nine_height_positions, new_pos)


def part_2_answer(lines):
    grid, size = parse(lines)

    return sum(trailhead_rating(grid, size, Position(x, y))
               for y, row in enumerate(grid)
               for x, cell in enumerate(row)
               if cell == 0)


def trailhead_rating(grid, size, trailhead):
    visited = set()
    distinct_trails = set()
    rating_search(grid, size, visited, distinct_trails, (trailhead,))
    return len(distinct_trails)


def rating_search(grid, size, visited, distinct_trails, path_so_far):
    visited.add(path_so_far)
    pos = path_so_far[-1]
    current_height = grid[pos.y][pos.x]

    if len(path_so_far) == 10:
        distinct_trails.add(path_so_far)

    for offset in UP, DOWN, LEFT, RIGHT:
        new_pos = Position(pos.x + offset.x, pos.y + offset.y)
        if (0 <= new_pos.x < size.width) and (0 <= new_pos.y < size.height):
            new_height = grid[new_pos.y][new_pos.x]
            if new_height == (current_height + 1):
                new_path_so_far = path_so_far + (new_pos,)
                if new_path_so_far not in visited:
                    rating_search(grid, size, visited, distinct_trails, new_path_so_far)


def parse(lines):
    grid = [[int(n) for n in line] for line in lines]
    size = Size(len(grid[0]), len(grid))
    return grid, size
