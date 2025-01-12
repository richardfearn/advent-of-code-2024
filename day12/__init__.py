from collections import deque
from collections import namedtuple

XY = namedtuple("XY", ["x", "y"])

Region = namedtuple("Region", ["plant_type", "points"])

UP, DOWN, LEFT, RIGHT = XY(0, -1), XY(0, 1), XY(-1, 0), XY(1, 0)


def part_1_answer(lines):
    grid_size, regions = find_regions(lines)
    return sum(part_1_price(region, lines, grid_size) for region in regions)


def part_1_price(region, grid, grid_size):
    return area(region) * perimeter(region, grid, grid_size)


def area(region):
    return len(region.points)


def perimeter(region, grid, grid_size):
    total = 0
    for x, y in region.points:
        for offset in UP, DOWN, LEFT, RIGHT:
            nx, ny = (x + offset.x), (y + offset.y)
            if (0 <= nx < grid_size.x) and (0 <= ny < grid_size.y):
                neighbour = grid[ny][nx]
                if neighbour != region.plant_type:
                    total += 1
            else:
                total += 1
    return total


# Some links I thought might be useful for part 2, but ultimately weren't:
#
#  * https://en.wikipedia.org/wiki/Rectilinear_polygon
#
#  * https://en.wikipedia.org/wiki/Orthogonal_convex_hull
#
#  * https://stackoverflow.com/questions/32496421/orthogonal-hull-algorithm
#
#  * https://math.stackexchange.com/questions/1354195/rectilinear-convex-hull


def part_2_answer(lines):
    _, regions = find_regions(lines)
    return sum(part_2_price(region) for region in regions)


def part_2_price(region):
    return area(region) * sides(region)


def sides(region):
    # pylint: disable=too-many-locals

    # Based on https://www.reddit.com/r/adventofcode/comments/1hcdnk0/comment/m1nio0w/

    points = region.points
    corners = 0

    for p in points:
        x, y = p

        x_west, x_east = [x + offset for offset in (-1, 1)]
        y_north, y_south = [y + offset for offset in (-1, 1)]

        north = (x, y_north)
        northeast = (x_east, y_north)
        east = (x_east, y)
        southeast = (x_east, y_south)
        south = (x, y_south)
        southwest = (x_west, y_south)
        west = (x_west, y)
        northwest = (x_west, y_north)

        # outer
        if (west not in points) and (north not in points):
            corners += 1
        if (east not in points) and (north not in points):
            corners += 1
        if (west not in points) and (south not in points):
            corners += 1
        if (east not in points) and (south not in points):
            corners += 1

        # inner
        if (west in points) and (north in points) and (northwest not in points):
            corners += 1
        if (east in points) and (north in points) and (northeast not in points):
            corners += 1
        if (west in points) and (south in points) and (southwest not in points):
            corners += 1
        if (east in points) and (south in points) and (southeast not in points):
            corners += 1

    return corners


def find_regions(lines):
    grid_size = XY(len(lines[0]), len(lines))

    visited = set()
    regions = []

    for y, row in enumerate(lines):
        for x, plant_type in enumerate(row):
            p = XY(x, y)
            if p not in visited:
                region_points = explore_region(lines, grid_size, visited, p, plant_type)
                regions.append(Region(plant_type, region_points))

    return grid_size, regions


def explore_region(lines, grid_size, visited, p, plant_type):
    region_points = set()
    to_visit = deque([p])

    while len(to_visit) > 0:
        p = to_visit.popleft()
        visited.add(p)
        region_points.add(p)

        for offset in UP, DOWN, LEFT, RIGHT:
            n = XY(p.x + offset.x, p.y + offset.y)
            if (0 <= n.x < grid_size.x) and (0 <= n.y < grid_size.y) and (n not in visited):
                neighbour = lines[n.y][n.x]
                if neighbour == plant_type:
                    visited.add(n)
                    to_visit.append(n)

    return region_points
