# coding: utf-8
import re
from helpers import read_input_file, run_func, test_func
bag_load = {"red":12,
            "blue":14,
            "green":13}


def ints_in_string(line):
    ii = list(map(int, re.findall(r"-?\d+", line)))
    return ii


def count_cubes_in_game(line):
    rounds = re.split(r"[;:]+", line)
    id = ints_in_string(rounds[0])[-1]
    r = 0
    g = 0
    b = 0
    for idx in range(len(rounds) - 1):
        shown = rounds[idx + 1]
        parts = shown.split(",")
        for part in parts:
            nb_cubes = ints_in_string(part)[0]
            if "red" in part:
                r = max(r, nb_cubes)
            elif "green" in part:
                g = max(g, nb_cubes)
            elif "blue" in part:
                b = max(b, nb_cubes)
    return id, r,g,b
def boom(input_val, DBG=True):
    ret = 0
    for line in input_val:
        id, r,g,b = count_cubes_in_game(line)
        if r <= 12 and g <= 13 and b <= 14:
            ret += id

    return ret


def boom2(input_val, DBG=True):
    ret = 0
    for line in input_val:
        _, r, g, b = count_cubes_in_game(line)
        ret += r * g * b
    return ret


#############

INPUT_FILE = "data/input-d02.txt"

puzzle_input = read_input_file(INPUT_FILE)
run_func(func=boom, puzzle_input=puzzle_input)
run_func(func=boom2, puzzle_input=puzzle_input)


input_test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""  ##
puzzle_test_input = input_test.splitlines()
test_func(boom2, cc=puzzle_test_input, expected=2286, DBG=False)

# PART 1 - 2563 OK
# PART 2 - 70768 OK
