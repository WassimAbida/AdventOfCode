# coding: utf-8
from helpers import read_input_file, run_func, test_func


def make_world():
    return


class F:
    """File type class, we only need to store the file size."""

    def __init__(self, size, name=""):
        self.size = size
        self.name = name


class D(F):
    """Directory type class, it contains a list of files."""

    def __init__(self, parent, name, size):
        self.parent = parent
        self.files = []
        self.name = name
        # self.size=0
        super().__init__(size=size)


def parse_dirs(input_val, DBG=False):
    root = D(None, name="/", size=0)
    curr_node = root
    del input_val[0]
    for line in input_val:
        if line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            pass
        elif line.startswith("$ cd .."):
            curr_node = curr_node.parent
        elif line.startswith("$ cd"):
            ll = line.split()
            d = D(curr_node, name=ll[2], size=0)
            curr_node.files.append(d)
            curr_node = d

        else:  # size file_name
            ll = line.split()
            file = F(size=int(ll[0]), name=ll[1])
            curr_node.files.append(file)
    if DBG:
        print("Hierarchy")
        print("-------")
        display_obj(root, space="")
    compute_dir_size(root)
    return root


def find_biggest_folders(tree, max_size):
    ret = []
    if isinstance(tree, D):
        if tree.size < max_size:
            ret.append(tree)
        for f in tree.files:
            ret.extend(find_biggest_folders(f, max_size))
    return ret


def compute_dir_size(root):
    if isinstance(root, D):
        for f in root.files:
            root.size += compute_dir_size(f)
    return root.size


def display_obj(object, space):

    if isinstance(object, D):
        if not object.parent:
            print(f"root (dir)")
        else:
            print(f"{space}{object.name} (dir)")
        space += "--"
        for elem in object.files:
            display_obj(elem, space=space)
    elif isinstance(object, F):
        print(f"{space}{object.name} (file, size={object.size})")


def boom(input_val, DBG=True):
    root = parse_dirs(input_val)
    biggest_dirs = find_biggest_folders(root, 100000)
    all_dir_size = [dir.size for dir in biggest_dirs]
    return sum(all_dir_size)


def boom2(input_val, DBG=True):
    FS_space = 70000000
    required_space = 30000000
    root = parse_dirs(input_val)

    remaining_space = FS_space - root.size

    biggest_dirs = find_biggest_folders(root, FS_space)
    ret = [d.size for d in biggest_dirs if remaining_space + d.size > 30000000]
    return min(ret)


#############

INPUT_FILE = "data/input-d07.txt"

puzzle_input = read_input_file(INPUT_FILE)
run_func(func=boom, puzzle_input=puzzle_input)
run_func(func=boom2, puzzle_input=puzzle_input)

input_test = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

tt1 = input_test.splitlines()
test_func(boom, cc=tt1, expected=95437, DBG=False)
test_func(boom2, cc=tt1, expected=24933642, DBG=False)

# PART 1 - 1749646 OK
# PART 2 - 1498966 OK
