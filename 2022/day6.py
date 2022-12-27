# coding: utf-8
from helpers import read_input_file, run_func, test_func


def last_four_character_are_diffrent(text):
    return len(set(text)) == len(text)

def find_starter(input_val, starter_length):
    for i in range(len(input_val)):
        text_sample = input_val[i : i + starter_length]
        if last_four_character_are_diffrent(text_sample):
            return i + starter_length

def boom(input_val, DBG=True):
    return find_starter(input_val, 4)


def boom2(input_val, DBG=True):
    return find_starter(input_val, 14)



#############

INPUT_FILE = "data/input-d06.txt"

puzzle_input = read_input_file(INPUT_FILE)
run_func(func=boom, puzzle_input=puzzle_input[0])

input_test = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]


for in_elem, out_elem in zip(input_test, [7, 5, 6, 10, 11]):
    test_func(boom, cc=in_elem, expected=out_elem, DBG=False)

for in_elem, out_elem in zip(input_test, [19, 23, 23, 29, 26]):
    test_func(boom2, cc=in_elem, expected=out_elem, DBG=False)

# PART 1 - 1080 OK
# PART 2 - 3645 OK
