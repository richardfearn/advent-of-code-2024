import re


def part_1_answer(lines):
    return part_1_scan("".join(lines))


def part_1_scan(memory):
    instructions = re.findall(r"mul\(\d+,\d+\)", memory)
    return sum(evaluate_mul_instruction(instruction) for instruction in instructions)


def part_2_answer(lines):
    return part_2_scan("".join(lines))


def part_2_scan(memory):
    total = 0
    enabled = True
    instructions = re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", memory)
    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif enabled:
            total += evaluate_mul_instruction(instruction)
    return total


def evaluate_mul_instruction(instruction):
    parameters = instruction[4:-1]
    a, b = parameters.split(",")
    return int(a) * int(b)
