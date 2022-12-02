# coding: utf-8
from helpers import *


def boom(input_val, DBG=True):

    elf_calories = 0
    elfs = []
    for elem in input_val:
        if elem:
            elf_calories += int(elem)
        else:
            elfs.append(elf_calories)
            elf_calories = 0
    return max(elfs)


def boom2():
    # Top 3 elfs calories
    # 212117
    # return sum(sorted(elfs, reverse=True)[:3])
    return


#############

INPUT_FILE = "data/input-d01.txt"
f = open(INPUT_FILE, "r")
contents = f.read()
puzzle_input = contents.splitlines()
f.close()
# ret = boom(puzzle_input, DBG=False)
run_func(func=boom, puzzle_input=puzzle_input)

# PART 1 - 72511 OK
# PART 2 - 212117 OK
