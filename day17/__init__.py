from enum import IntEnum, auto


class Operand(IntEnum):
    adv = 0
    bxl = auto()
    bst = auto()
    jnz = auto()
    bxc = auto()
    out = auto()
    bdv = auto()
    cdv = auto()


def part_1_answer(lines):
    (a, b, c), program = parse(lines)
    _, output = run((a, b, c), program)
    return ",".join(str(n) for n in output)


def run(registers, program):
    a, b, c = registers
    ip = 0
    output = []

    while True:

        if ip >= len(program):
            break

        opcode = program[ip]
        operand = program[ip + 1]
        ip += 2

        if opcode == Operand.adv:
            a = a // (2 ** combo_operand(operand, a, b, c))

        elif opcode == Operand.bxl:
            b = b ^ operand

        elif opcode == Operand.bst:
            b = combo_operand(operand, a, b, c) % 8

        elif opcode == Operand.jnz:
            if a != 0:
                ip = operand

        elif opcode == Operand.bxc:
            b = b ^ c

        elif opcode == Operand.out:
            output.append(combo_operand(operand, a, b, c) % 8)

        elif opcode == Operand.bdv:
            b = a // (2 ** combo_operand(operand, a, b, c))

        elif opcode == Operand.cdv:
            c = a // (2 ** combo_operand(operand, a, b, c))

    return (a, b, c), output


def combo_operand(operand, a, b, c):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c

    raise AssertionError(f"Invalid combo operand {operand}")


def part_2_answer(lines):
    _, program = parse(lines)
    return part_2_dfs(program, 15, 0)


def part_2_dfs(program, pos, a):
    a <<= 3

    num_iterations = 16 - pos

    for candidate in range(8):

        new_a = a + candidate
        output = run_input_program(new_a, num_iterations)

        if pos == 0:
            if output == program:
                return new_a

        else:
            actual = output[-num_iterations:]
            expected = program[-num_iterations:]

            if actual == expected:
                result = part_2_dfs(program, pos - 1, new_a)
                if result is not None:
                    return result

    return None


def run_input_program(a, iterations):
    output = []

    for _ in range(iterations):
        b = a % 8
        b = b ^ 7
        c = a // (2 ** b)
        a = a // 8
        b = b ^ 7
        b = b ^ c
        output.append(b % 8)

    return output


def parse(lines):
    registers = [int(line.split(": ")[1]) for line in lines[:3]]
    program = [int(n) for n in lines[4].split(": ")[1].split(",")]
    return registers, program
