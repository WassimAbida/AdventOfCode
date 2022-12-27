# coding: utf-8
from helpers import *

def pair_to_range(pair:str):
    x, y = pair.split('-')
    return range(int(x),int(y)+1)

def list_contain_another_list(L1,L2):
    return all(item in L1 for item in L2)

def boom(input_val, DBG=True):
    sum_absorbed = 0
    for line in input_val:
        pair1, pair2 = line.split(',')
        range1 = pair_to_range(pair1)
        range2 = pair_to_range(pair2)

        check = list_contain_another_list(range1, range2) or list_contain_another_list(range2, range1)
        if check:
            sum_absorbed+=1
        # 5-71,2-3
    return sum_absorbed



def boom2(input_val, DBG=True):

    ## overlaps
    sum_overlaps = 0
    for line in input_val:
        pair1, pair2 = line.split(',')
        range1 = set(pair_to_range(pair1))
        range2 = set(pair_to_range(pair2))
        overlap = set(range1).intersection(range2)
        if overlap:
            sum_overlaps+=1

    return sum_overlaps


#############

INPUT_FILE = "data/input-d04.txt"
f = open(INPUT_FILE, "r")
contents = f.read()
puzzle_input = contents.splitlines()
f.close()
# ret = boom(puzzle_input, DBG=False)
run_func(func=boom2, puzzle_input=puzzle_input)

##
input_test = ["2-4,6-8",
"2-3,4-5",
"5-7,7-9",
"2-8,3-7",
"6-6,4-6",
"2-6,4-8"]
test_func(boom2, cc=input_test, expected=4, DBG=False)

# PART 1 - 424 OK
# PART 2 - 12725 OK
