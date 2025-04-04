# coding: utf-8
from helpers import read_input_file, run_func, test_func


def make_complex_world(input_val, DBG=True):
    x_min, x_max, y_min, y_max = 0, len(input_val[0]), 0, len(input_val)
    field = {complex(x, y): input_val[y][x] for y in range(y_max) for x in range(x_max)}
    directions = [complex(0, 1) ** i for i in range(4)]
    return field, x_min, x_max, y_min, y_max, directions


def is_visible(field, x, y, directions):
    z0 = complex(x, y)
    for dz in directions:
        current_z = z0
        visible = True
        while True:
            current_z = current_z + dz
            if current_z not in field:
                if visible:
                    return True
                break
            if field[current_z] >= field[z0]:
                visible = False
                break
    return False


def boom(input_val, DBG=True):
    field, x_min, x_max, y_min, y_max, directions = make_complex_world(input_val)

    return sum(
        [
            is_visible(field, x, y, directions)
            for x in range(x_min, x_max)
            for y in range(y_min, y_max)
        ]
    )


def boom2(input_val, DBG=True):
    field, x_min, x_max, y_min, y_max, directions = make_complex_world(input_val)

    return max(
        [
            compute_scenic_score(field, x, y, directions)
            for x in range(x_min, x_max)
            for y in range(y_min, y_max)
        ]
    )


def compute_scenic_score(field, x, y, directions):
    z0 = complex(x,y)
    scenic_score=1
    for dz in directions:
        view_distance = 0
        current_z = z0
        while True:
            current_z += dz
            if current_z not in field:
                break
            view_distance += 1
            if field[current_z] >= field[z0]:
                break
        scenic_score *= view_distance
    return scenic_score




#############

INPUT_FILE = "data/input-d08.txt"

puzzle_input = read_input_file(INPUT_FILE)
run_func(func=boom, puzzle_input=puzzle_input)
run_func(func=boom2, puzzle_input=puzzle_input)

input_test = """30373
25512
65332
33549
35390"""  ##
tt1 = input_test.splitlines()
test_func(boom, cc=tt1, expected=21, DBG=False)
test_func(boom2, cc=tt1, expected=8, DBG=False)

# PART 1 - xx OK
# PART 2 - xxx OK