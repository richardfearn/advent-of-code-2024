from collections import deque, defaultdict, namedtuple
from heapq import heappush, heappop

XY = namedtuple("XY", ["x", "y"])
State = namedtuple("State", ["pos", "direction"])

LEFT, RIGHT, UP, DOWN = XY(-1, 0), XY(1, 0), XY(0, -1), XY(0, 1)

CLOCKWISE = {
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP,
    UP: RIGHT,
}

ANTICLOCKWISE = {
    RIGHT: UP,
    UP: LEFT,
    LEFT: DOWN,
    DOWN: RIGHT,
}


def part_1_answer(lines):
    grid = parse(lines)
    size = XY(len(grid[0]), len(grid))
    start_pos, end_pos = find_start_and_end(grid)

    edges = build_graph(grid, size, start_pos)
    distances = shortest_path(start_pos, edges)

    return min(dist for (node, dist) in distances.items() if node.pos == end_pos)


def find_start_and_end(grid):
    start_pos = end_pos = None

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "S":
                start_pos = XY(x, y)
            if cell == "E":
                end_pos = XY(x, y)

    grid[start_pos.y][start_pos.x] = '.'
    grid[end_pos.y][end_pos.x] = '.'

    return start_pos, end_pos


def part_1_neighbours(grid, size, state):
    pos, current_dir = state

    yield State(pos, CLOCKWISE[current_dir])
    yield State(pos, ANTICLOCKWISE[current_dir])

    forward_pos = XY(pos.x + current_dir.x, pos.y + current_dir.y)
    if (0 < forward_pos.x < size.x) and (0 < forward_pos.y < size.y):
        if grid[forward_pos.y][forward_pos.x] != "#":
            yield State(forward_pos, current_dir)


def build_graph(grid, size, start_pos, start_dir=RIGHT, neighbour_function=part_1_neighbours):
    start = State(start_pos, start_dir)

    edges = defaultdict(set)

    to_visit = deque([start])
    visited = {start}

    while len(to_visit) > 0:
        current = to_visit.popleft()

        for neighbour in neighbour_function(grid, size, current):
            edges[current].add(neighbour)
            if neighbour not in visited:
                visited.add(neighbour)
                to_visit.append(neighbour)

    return edges


def shortest_path(start_pos, edges, direction=RIGHT):
    start = State(start_pos, direction)

    dist = {start: 0}
    q = [(0, start)]

    while len(q) > 0:
        u = heappop(q)[1]
        for v in edges[u]:
            alt = dist[u] + score(u, v)
            if (v not in dist) or (alt < dist[v]):
                dist[v] = alt
                heappush(q, (alt, v))

    return dist


def score(u, v):
    return 1000 if (u.pos == v.pos) else 1


def part_2_answer(lines):
    grid = parse(lines)
    size = XY(len(grid[0]), len(grid))
    start_pos, end_pos = find_start_and_end(grid)

    edges_forward = build_graph(grid, size, start_pos, RIGHT, part_1_neighbours)
    forward_distances = shortest_path(start_pos, edges_forward)
    min_dist = min(dist for (node, dist) in forward_distances.items() if node.pos == end_pos)

    end_nodes = [node for (node, dist) in forward_distances.items() if (node.pos == end_pos) and (dist == min_dist)]
    assert len(end_nodes) == 1
    end_node = end_nodes[0]

    edges_backward = build_graph(grid, size, end_node.pos, end_node.direction, part_2_neighbours_reverse)
    reverse_distances = shortest_path(end_pos, edges_backward, direction=end_node.direction)

    return len(find_nodes_on_shortest_path(size, forward_distances, reverse_distances, min_dist))


def part_2_neighbours_reverse(grid, size, state):
    pos, current_dir = state

    yield State(pos, CLOCKWISE[current_dir])
    yield State(pos, ANTICLOCKWISE[current_dir])

    reverse_pos = XY(pos.x - current_dir.x, pos.y - current_dir.y)
    if (0 < reverse_pos.x < size.x) and (0 < reverse_pos.y < size.y):
        if grid[reverse_pos.y][reverse_pos.x] != "#":
            yield State(reverse_pos, current_dir)


def find_nodes_on_shortest_path(size, forward_distances, reverse_distances, min_dist):
    on_shortest_path = set()

    for y in range(size.y):
        for x in range(size.x):
            pos = XY(x, y)
            for direction in LEFT, RIGHT, DOWN, UP:
                node = State(pos, direction)
                if (node in forward_distances) and (node in reverse_distances):
                    dist = forward_distances[node] + reverse_distances[node]
                    if dist == min_dist:
                        on_shortest_path.add(pos)

    return on_shortest_path


def parse(lines):
    return [list(row) for row in lines]
