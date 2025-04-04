# coding: utf-8
from helpers import read_input_file, run_func, test_func
import re 

def boom(input_val, DBG=True):
    pattern = r"mul[\(\[\{\<]\s*(\d+)\s*,\s*(\d+)\s*[\)\]\}\>]"
    pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

    if isinstance(input_val,str):
        input_val = [input_val]
    total_sum = 0
    for text_line in input_val:
        matches = re.findall(pattern, text_line)
        total_sum += sum(int(x) * int(y) for x, y in matches)
    return total_sum


def boom2(input_val, DBG=True):

    if isinstance(input_val,str):
        input_val = [input_val]
    for text_line in input_val:
        muls = re.findall(r"(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))", text_line)
        factor = 1
        products, factors = [], []
        print(muls)
        for mul, do, dont in muls:
            
            if dont != "":
                factor = 0

            elif do != "":
                factor = 1
            else:
                ii = list(map(int, re.findall(r"-?\d+", mul)))
                products.append(ii[0] * ii[1])
                factors.append(factor)
        print(products)
        print(factors)

    return sum([p*f for p, f in zip(products, factors)])


#############

INPUT_FILE = "data/input-d03.txt"

puzzle_input = read_input_file(INPUT_FILE)
run_func(func=boom2, puzzle_input=puzzle_input)

input_test = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""  ##
test_func(boom2, cc=input_test, expected=48, DBG=False)

# PART 1 - 182780583 OK
# PART 2 - 20865931 OK



import re

# ipt="""xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
# ipt="""xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
ipt = open(INPUT_FILE).read()

muls = re.findall(r"(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))", ipt)

factor = 1
products, factors = [], []
for mul, do, dont in muls:
    if dont != "":
                factor = 1 - factor

    elif  do != "":
                factor = 1
    else:
        ii = list(map(int, re.findall(r"-?\d+", mul)))
        products.append(ii[0] * ii[1])
        factors.append(factor)

print(f"# Part 1 solution: {sum(products)}")
print(f"# Part 2 solution: {sum([p * f for p, f in zip(products, factors)])}")