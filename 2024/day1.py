# coding: utf-8
from helpers import *


def boom(input_val, DBG=True):
    left_list, right_list = input_val[0], input_val[1]

    left_list.sort()
    right_list.sort()

    d = 0
    for i, elem in enumerate(right_list):
        d += abs(elem - left_list[i])
    return d

from collections import Counter
def boom2(input_val, DBG):
    similarity_score = 0
    left_list, right_list = input_val[0], input_val[1]

    values = left_list
    counts = Counter(right_list)

    for elem in values:
        similarity_score += elem * counts.get(elem, 0)
        
    return similarity_score


#############

INPUT_FILE = "./data/input-d01.txt"

def load_seperate_lists(file_name):

    left_list = []
    right_list = []

    with open(file_name, "r") as file:
        for line in file:
            left, right = map(int, line.split())  # Split and convert to integers
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

left_list, right_list = load_seperate_lists(INPUT_FILE)
run_func(func=boom2, puzzle_input=(left_list, right_list))

input_test = """3   4
4   3
2   5
1   3
3   9
3   3"""  
tt1 = input_test.splitlines()
tt1 = ([3,4,2,1,3,3], [4,3,5,3,9,3])
test_func(boom2, cc=tt1, expected=31, DBG=False)

# PART 1 - 1110981 OK
# PART 2 - 24869388 OK
