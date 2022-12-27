# coding: utf-8
from helpers import *
from collections import Counter

def get_common_member_in_rucksack(rucksack:str):
    rucksack_p1 = rucksack[:len(rucksack) // 2]
    rucksack_p2 = rucksack[len(rucksack) // 2 :]

    print(rucksack_p1, rucksack_p2)
    p1 = set(rucksack_p1)
    p2 = set(rucksack_p2)
    return p1.intersection(p2)

# Generate lowercase Mapping
SCORES = {chr(i+96): i for i in range(1,27)}
# Generate UPPERCASE Mapping
SCORES.update({chr(i+64): i+26 for i in range(1,27)})
print(SCORES)

def boom(input_val, DBG=True):
    sum_priorities = 0
    for rucksack in input_val:
        common_member = get_common_member_in_rucksack(rucksack)
        for elem in common_member:
            sum_priorities+=SCORES[elem]
            print(rucksack , elem, SCORES[elem], sum_priorities)

    return sum_priorities


def divide_chunks(input_list, n):
    # looping till length l
    for i in range(0, len(input_list), n):
        yield input_list[i:i + n]

def boom2(input_val, DBG=True):
    elfs = list(divide_chunks(input_val,3))

    sum_priorities = 0
    for batch in elfs:
        p0 = set(batch[0])
        p1 = set(batch[1])
        p2 = set(batch[2])
        set4 = p0 & p1 & p2
        sum_priorities+=SCORES[next(iter(set4))]

    return sum_priorities



##
input_test = ["vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg",
                "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw"]

test_func(boom2, cc=input_test, expected=70, DBG=False)


#############

INPUT_FILE = "data/input-d03.txt"
f = open(INPUT_FILE, "r")
contents = f.read()
puzzle_input = contents.splitlines()
f.close()
# ret = boom(puzzle_input, DBG=False)
run_func(func=boom, puzzle_input=puzzle_input)

# PART 1 - 8185 OK
# PART 2 - 2817 OK
