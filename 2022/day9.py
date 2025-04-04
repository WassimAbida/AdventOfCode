# coding: utf-8
from helpers import read_input_file, run_func, test_func


def boom(input_val, DBG=True):
    return ""


def boom2(input_val, DBG=True):
    return ""


#############

INPUT_FILE = "data/input-d0x.txt"

puzzle_input = read_input_file(INPUT_FILE)
run_func(func=boom, puzzle_input=puzzle_input)

input_test = ""  ##
test_func(boom, cc=input_test, expected=12, DBG=False)

# PART 1 - xx OK
# PART 2 - xxx OK
