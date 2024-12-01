def part_1_answer(lines):
    lines = [line.split() for line in lines]
    numbers = [(int(line[0]), int(line[1])) for line in lines]
    left, right = zip(*numbers)
    left = sorted(left)
    right = sorted(right)
    return sum(abs(right_num - left_num) for (left_num, right_num) in zip(left, right))


def part_2_answer(lines):
    lines = [line.split() for line in lines]
    numbers = [(int(line[0]), int(line[1])) for line in lines]
    left, right = zip(*numbers)
    return sum(left_num * right.count(left_num) for left_num in left)
