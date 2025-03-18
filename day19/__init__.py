from functools import cache


def part_1_answer(lines):
    towels, patterns = parse(lines)
    return sum(1 for pattern in patterns if part_1_dfs(towels, pattern))


def part_1_dfs(towels, pattern):
    if pattern == "":
        return True
    return any(is_possible(towels, pattern, towel) for towel in towels if pattern.startswith(towel))


def is_possible(towels, pattern, towel):
    remaining = pattern[len(towel):]
    return part_1_dfs(towels, remaining)


def part_2_answer(lines):
    towels, patterns = parse(lines)
    return sum(part_2_dfs(tuple(towels), pattern) for pattern in patterns)


@cache
def part_2_dfs(towels, pattern):
    if pattern == "":
        return 1
    return sum(num_ways(towels, pattern, towel) for towel in towels if pattern.startswith(towel))


def num_ways(towels, pattern, towel):
    remaining = pattern[len(towel):]
    return part_2_dfs(towels, remaining)


def parse(lines):
    towels = lines[0].split(", ")
    patterns = lines[2:]
    return towels, patterns
