from collections import defaultdict, namedtuple, deque
from heapq import heappop, heappush

XY = namedtuple("XY", ["x", "y"])

UP, DOWN, LEFT, RIGHT = XY(0, -1), XY(0, 1), XY(-1, 0), XY(1, 0)


def part_1_answer(lines, size, fallen):
    byte_positions = parse(lines)

    corrupted = set(byte_positions[:fallen])

    start_pos = XY(0, 0)
    end_pos = XY(size - 1, size - 1)

    nodes = set()
    edges = defaultdict(set)

    for x in range(size):
        for y in range(size):
            pos = XY(x, y)
            if pos not in corrupted:
                nodes.add(pos)
                for direction in (UP, DOWN, LEFT, RIGHT):
                    neighbour = XY(x + direction.x, y + direction.y)
                    if (0 <= neighbour.x < size) and (0 <= neighbour.y < size) and (neighbour not in corrupted):
                        edges[pos].add(neighbour)
                        edges[neighbour].add(pos)

    dist = shortest_path(start_pos, edges)
    return dist[end_pos]


# pylint: disable=duplicate-code
def shortest_path(start, edges):
    dist = {start: 0}
    q = [(0, start)]

    while len(q) > 0:
        u = heappop(q)[1]
        for v in edges[u]:
            alt = dist[u] + 1
            if (v not in dist) or (alt < dist[v]):
                dist[v] = alt
                heappush(q, (alt, v))

    return dist


def part_2_answer(lines, size):
    byte_positions = parse(lines)

    left, right = 0, len(byte_positions) - 1
    while left <= right:
        mid = (left + right) // 2

        if can_reach_exit(byte_positions[:mid], size):
            left = mid + 1
        else:
            right = mid - 1

    answer = byte_positions[left - 1]
    return f"{answer[0]},{answer[1]}"


def can_reach_exit(corrupted, size):
    corrupted = set(corrupted)

    start_pos = XY(0, 0)
    end_pos = XY(size - 1, size - 1)

    to_visit = deque([start_pos])
    visited = {start_pos}

    while len(to_visit) > 0:
        p = to_visit.popleft()
        for direction in (UP, DOWN, LEFT, RIGHT):
            neighbour = XY(p.x + direction.x, p.y + direction.y)
            if (0 <= neighbour.x < size) and (0 <= neighbour.y < size):
                if (neighbour not in visited) and (neighbour not in corrupted):
                    to_visit.append(neighbour)
                    visited.add(neighbour)

    return end_pos in visited


def parse(lines):
    positions = [tuple(int(n) for n in line.split(",")) for line in lines]
    return [XY(*pos) for pos in positions]
