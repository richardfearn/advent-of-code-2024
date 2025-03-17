import itertools
import statistics
from collections import namedtuple

XY = namedtuple("XY", ["x", "y"])
Robot = namedtuple("Robot", ["p", "v"])


def part_1_answer(lines, width, height, steps):
    robots = parse(lines)
    grid_size = XY(width, height)

    final_positions = [final_position(robot, grid_size, steps) for robot in robots]

    mid = XY(grid_size.x // 2, grid_size.y // 2)

    top_left = sum(1 for p in final_positions if (p.x < mid.x) and (p.y < mid.y))
    top_right = sum(1 for p in final_positions if (p.x > mid.x) and (p.y < mid.y))
    bottom_left = sum(1 for p in final_positions if (p.x < mid.x) and (p.y > mid.y))
    bottom_right = sum(1 for p in final_positions if (p.x > mid.x) and (p.y > mid.y))

    return top_left * top_right * bottom_left * bottom_right


def final_position(robot, grid_size, steps):
    return XY((robot.p.x + steps * robot.v.x) % grid_size.x,
              (robot.p.y + steps * robot.v.y) % grid_size.y)


def part_2_answer(lines, width, height):
    robots = parse(lines)
    grid_size = XY(width, height)

    for steps in itertools.count(1):
        final_positions = [final_position(robot, grid_size, steps) for robot in robots]

        x_vals = [p.x for p in final_positions]
        y_vals = [p.y for p in final_positions]

        x_std_dev = statistics.stdev(x_vals)
        y_std_dev = statistics.stdev(y_vals)

        if (x_std_dev < 25) and (y_std_dev < 25):
            return steps

    return None


def parse(lines):
    return [parse_line(line) for line in lines]


def parse_line(line):
    p, v = [pos_or_velocity[2:] for pos_or_velocity in line.split(" ")]
    p = [int(n) for n in p.split(",")]
    v = [int(n) for n in v.split(",")]
    return Robot(p=XY(*p), v=XY(*v))
