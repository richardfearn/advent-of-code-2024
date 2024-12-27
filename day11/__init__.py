from functools import cache


def part_1_answer(lines):
    stones = parse(lines)
    return num_after_blinking(stones, 25)


def part_2_answer(lines):
    stones = parse(lines)
    return num_after_blinking(stones, 75)


def num_after_blinking(stones, num_blinks):
    return sum(total_stones(stone, num_blinks) for stone in stones)


@cache
def total_stones(stone, blinks_remaining):
    if blinks_remaining == 0:
        return 1

    if stone == 0:
        return total_stones(1, blinks_remaining - 1)

    if has_even_number_of_digits(stone):
        left, right = split(stone)
        return (total_stones(left, blinks_remaining - 1) +
                total_stones(right, blinks_remaining - 1))

    return total_stones(stone * 2024, blinks_remaining - 1)


def has_even_number_of_digits(n):
    return (len(str(n)) % 2) == 0


def split(n):
    chars = str(n)
    mid = len(chars) // 2
    return int(chars[:mid]), int(chars[mid:])


def parse(lines):
    return [int(n) for n in lines[0].split(" ")]
