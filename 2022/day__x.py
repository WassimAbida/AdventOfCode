# coding: utf-8
from helpers import *



def boom(input_val, DBG=True):
    return input_val



def boom2(input_val, DBG=True):
    return input_val


#############

INPUT_FILE = "data/input-d02.txt"
f = open(INPUT_FILE, "r")
contents = f.read()
puzzle_input = contents.splitlines()
f.close()
# ret = boom(puzzle_input, DBG=False)
run_func(func=boom2, puzzle_input=puzzle_input)

##
input_test = ["A Y", "B X", "C Z"]
test_func(boom2, cc=input_test, expected=12, DBG=False)

# PART 1 - 11603 OK
# PART 2 - 12725 OK
