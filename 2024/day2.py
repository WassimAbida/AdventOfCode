# coding: utf-8
from helpers import *


def is_increasing(L):
    return all(L[i]  < L[i+1] for i in range(len(L)-1))

def is_decreasing(L):
    return all(L[i]  > L[i+1] for i in range(len(L)-1))

def diff_compute(L):
    return all(0 < abs(L[i+1] - L[i])<=3 for i in range(len(L)-1) )


def is_safe(L):
    return (is_decreasing(L) or is_increasing(L)) and diff_compute(L)

def boom(input_val, DBG=True):
    return sum(1 for report in input_val  if is_safe(list(map(int, report.split(" "))) ))


def boom2(input_val, DBG=True):

    count_safe = 0
    for report in input_val:
        report_nums = list(map(int,report.split(" ")))

        for i in range(len(report_nums)):
            mid_level = report_nums[:i] + report_nums[i+1:]
            if is_safe(mid_level):
                count_safe+=1
                break


    return count_safe


#############

INPUT_FILE = "./data/input-d02.txt"
puzzle_input = read_input_file(INPUT_FILE)
run_func(func=boom2, puzzle_input=puzzle_input)

input_test = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""  

tt1 = input_test.splitlines()
test_func(boom2, cc=tt1, expected=4, DBG=False)

# PART 1 - 1110981 OK
# PART 2 - 24869388 OK
