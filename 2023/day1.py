# coding: utf-8
from helpers import read_input_file, run_func, test_func


def boom(input_val, DBG=True):
    list_digits = []
    for elem in input_val:
        digits = []
        for ix in elem:
            if ix.isdigit():
                digits+=ix
        list_digits.append(int(digits[0]+digits[-1]))
    return sum(list_digits)

word_to_int = {
    'zero': "0",
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def boom2(input_val, DBG=True):
    digit_to_digit = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    calibration_total = 0
    for line in input_val:
        digits_in_line = []
        for i in range(len(line)):
            for k, v in digit_to_digit.items():
                if line[i:].startswith(k):
                    digits_in_line.append(v)
        if DBG:
            print(digits_in_line)
        calibration_total += int(digits_in_line[0] + digits_in_line[-1])
    return calibration_total


#############

INPUT_FILE = "data/input-d01.txt"

puzzle_input = read_input_file(INPUT_FILE)
run_func(func=boom2, puzzle_input=puzzle_input)

input_test = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""  ##

puzzle_test_input = input_test.splitlines()
test_func(boom2, cc=puzzle_test_input, expected=281, DBG=False)

# PART 1 - 55002 OK
# PART 2 - 55093 OK
