# coding: utf-8
from helpers import *

options = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

options_scores = {"Rock": 1, "Paper": 2, "Scissors": 3}


def rules(e_1, e_2):
    if options[e_1] == options[e_2]:
        return 3  # draw
    elif options[e_1] == "Rock" and options[e_2] == "Paper":
        return 6  # win
    elif options[e_1] == "Rock" and options[e_2] == "Scissors":
        return 0  # loss

    elif options[e_1] == "Paper" and options[e_2] == "Rock":
        return 0  # loss
    elif options[e_1] == "Paper" and options[e_2] == "Scissors":
        return 6  # win

    elif options[e_1] == "Scissors" and options[e_2] == "Rock":
        return 6  # win
    elif options[e_1] == "Scissors" and options[e_2] == "Paper":
        return 0  # loss
    else:
        raise ("Invalid")


def boom(input_val, DBG=True):

    final_score = 0
    for line in input_val:
        op_1, op_2 = tuple(line.split(" "))
        round_score = rules(op_1, op_2)
        print(op_1, op_2, round_score, options_scores[options[op_2]])
        final_score += options_scores[options[op_2]]
        final_score += round_score
    return final_score
    # lost, draw, win


round_status = {"X": 0, "Y": 3, "Z": 6}

win_scene = {"C": "X", "A": "Y", "B": "Z"}
loss_scene = {"C": "Y", "B": "X", "A": "Z"}


def boom2(input_val, DBG=True):
    final_score = 0
    for line in input_val:
        op_1, op_2 = tuple(line.split(" "))
        score_op2_choice = 0
        if op_2 == "X":
            # lose
            op2_choice = loss_scene[op_1]
            score_op2_choice = options_scores[options[op2_choice]]
        elif op_2 == "Y":
            # draw
            # Get the score of my opponnet choice
            score_op2_choice = 3 + options_scores[options[op_1]]
        elif op_2 == "Z":
            # win
            op2_choice = win_scene[op_1]
            score_op2_choice = 6 + options_scores[options[op2_choice]]
        final_score += score_op2_choice
    return final_score


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
