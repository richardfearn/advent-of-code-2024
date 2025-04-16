import itertools
from collections import namedtuple
from enum import IntEnum, auto
from functools import cache

XY = namedtuple("XY", ["x", "y"])


class KeypadType(IntEnum):
    NUMERIC = auto()
    DIRECTIONAL = auto()


class Keypad:
    # pylint: disable=too-few-public-methods

    def __init__(self, keypad_type, layout):
        self.type = keypad_type

        self.button_positions = {}
        lines = layout.strip("\n").split("\n")
        for y, row in enumerate(lines):
            for x, char in enumerate(row):
                pos = XY(x, y)
                if char != " ":
                    self.button_positions[char] = pos

    def position_of(self, button):
        return self.button_positions[button]


NUMERIC_KEYPAD_LAYOUT = """
789
456
123
 0A
"""

DIRECTIONAL_KEYPAD_LAYOUT = """
 ^A
<v>
"""

NUMERIC_KEYPAD = Keypad(KeypadType.NUMERIC, NUMERIC_KEYPAD_LAYOUT)

DIRECTIONAL_KEYPAD = Keypad(KeypadType.DIRECTIONAL, DIRECTIONAL_KEYPAD_LAYOUT)

KEYPADS = {keypad.type: keypad for keypad in (NUMERIC_KEYPAD, DIRECTIONAL_KEYPAD)}

OFFSETS = {
    "<": XY(-1, 0),
    ">": XY(1, 0),
    "^": XY(0, -1),
    "v": XY(0, 1),
}

A = "A"


def part_1_answer(lines):
    return sum_of_complexities(lines, 2)


def part_2_answer(lines):
    return sum_of_complexities(lines, 25)


def sum_of_complexities(codes, robot_directional_keypads):
    return sum(code_complexity(code, robot_directional_keypads) for code in codes)


def code_complexity(code, robot_directional_keypads):
    return min_presses_inc_numeric(code, robot_directional_keypads) * numeric_part(code)


def min_presses_inc_numeric(code, robot_directional_keypads):
    numeric_keypad_sequence = find_numeric_keypad_sequence(code)
    return min_presses_directional_only(numeric_keypad_sequence, robot_directional_keypads)


def min_presses_directional_only(sequence, robot_num):
    return sum(find_num_presses(button1, button2, robot_num) for button1, button2 in itertools.pairwise(A + sequence))


@cache
def find_num_presses(current_button, next_button, robot_num):
    current_pos = DIRECTIONAL_KEYPAD.position_of(current_button)
    _, subsequence = find_sequence(current_pos, next_button, KeypadType.DIRECTIONAL)
    subsequence += A

    if robot_num == 1:
        return len(subsequence)

    return min_presses_directional_only(subsequence, robot_num - 1)


def find_numeric_keypad_sequence(code):
    robot_pos = NUMERIC_KEYPAD.position_of(A)
    sequence = ""

    for char in code:
        robot_pos, subsequence = find_sequence(robot_pos, char, KeypadType.NUMERIC)
        sequence += subsequence + A

    return sequence


@cache
def find_sequence(current_pos, next_button, keypad_type):
    # pylint: disable=too-many-locals,too-many-return-statements,too-many-branches

    # https://www.reddit.com/r/adventofcode/comments/1hjgyps/2024_day_21_part_2_i_got_greedyish/

    keypad = KEYPADS[keypad_type]

    next_pos = keypad.position_of(next_button)

    horizontal_move = next_pos.x - current_pos.x
    vertical_move = next_pos.y - current_pos.y

    moving_horizontally = horizontal_move != 0
    moving_vertically = vertical_move != 0

    is_up = vertical_move < 0
    is_down = vertical_move > 0
    is_left = horizontal_move < 0
    is_right = horizontal_move > 0

    # Special case for no move

    if (not moving_horizontally) and (not moving_vertically):
        return next_pos, ""

    # Determine updo/leri strings

    updo = leri = ""

    if moving_vertically:
        button_to_press = "^" if is_up else "v"
        updo = button_to_press * abs(vertical_move)

    if moving_horizontally:
        button_to_press = "<" if is_left else ">"
        leri = button_to_press * abs(horizontal_move)

    # If either updo or leri is empty, return the other one

    if not moving_horizontally:
        return next_pos, updo

    if not moving_vertically:
        return next_pos, leri

    # Numeric keypad exclusive rule

    if keypad_type == KeypadType.NUMERIC:

        # On the bottom row and going to the left column
        if (current_pos.y == 3) and (next_pos.x == 0):
            return next_pos, updo + leri

        # In the far-left column and travelling to the bottom row
        if (current_pos.x == 0) and (next_pos.y == 3):
            return next_pos, leri + updo

    # Directional keypad exclusive rule

    if keypad_type == KeypadType.DIRECTIONAL:

        # Starting on the farthest left column
        if current_pos.x == 0:
            return next_pos, leri + updo

        # Traveling to the farthest left column
        if next_pos.x == 0:
            return next_pos, updo + leri

    # General case rules

    if is_up and is_left:
        return next_pos, leri + updo

    if is_down and is_left:
        return next_pos, leri + updo

    if is_down and is_right:
        return next_pos, updo + leri

    if is_up and is_right:
        return next_pos, updo + leri

    return None


def numeric_part(code):
    return int("".join(c for c in code if str.isdigit(c)), 10)
