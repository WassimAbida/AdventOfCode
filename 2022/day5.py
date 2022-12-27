# coding: utf-8
from helpers import *
from collections import defaultdict, deque
import re


def make_world(input_val, DBG=False):
    """Create World, get stacks & instructions."""

    stacks = defaultdict(deque)
    idx = 0
    while True:
        line = input_val[idx]
        idx += 1
        if line.startswith(" 1 "):
            idx += 1
            break
        for j in range((1 + len(line)) // 4):
            if line[j * 4 + 1] != " ":
                stacks[j + 1].appendleft(line[j * 4 + 1])
    if DBG:
        print("Stacks:", stacks)
    instructions = []
    while idx < len(input_val):
        line = input_val[idx]
        idx += 1
        nb_crates, from_stack, to_stack = map(int, re.findall(r"\d+", line))
        # move 2 from 2 to 1 ==> 2,2,1
        # \d+ matches a digit one or multiple times in str line
        instructions.append((nb_crates, from_stack, to_stack))
    if DBG:
        print("Instructions:", instructions)
    return stacks, instructions


def process_instructions(stacks, instructions, reverse=False):
    for instruct in instructions:
        nb_crates, from_stack, to_stack = instruct
        crates_list = []
        for _ in range(nb_crates):
            crate = stacks[from_stack].pop()
            crates_list.append(crate)
        if reverse:
            crates_list = reversed(crates_list)

        stacks[to_stack].extend(crates_list)

    return stacks


def get_top_stacks(stacks):
    top_stacks = ""
    for i in range(len(stacks)):
        last_elem = stacks[i + 1][-1]
        top_stacks += last_elem
    return top_stacks


def boom(input_val, DBG=True):
    stacks, instructions = make_world(input_val, DBG=DBG)
    processed_stacks = process_instructions(stacks, instructions, reverse=False)
    return get_top_stacks(processed_stacks)


def boom2(input_val, DBG=True):
    stacks, instructions = make_world(input_val, DBG=DBG)
    processed_stacks = process_instructions(stacks, instructions, reverse=True)
    return get_top_stacks(processed_stacks)


#############

INPUT_FILE = "data/input-d05.txt"
f = open(INPUT_FILE, "r")
contents = f.read()
puzzle_input = contents.splitlines()
f.close()

run_func(func=boom2, puzzle_input=puzzle_input)

##
t1 = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
 
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""  # noqa
tt1 = t1.splitlines()
# input_test = ["A Y", "B X", "C Z"]
test_func(boom2, cc=tt1, expected="MCD", DBG=False)

# PART 1 - RFFFWBPNS OK
# PART 2 - CQQBBJFCS OK
