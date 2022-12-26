import re
import sys


SIZE_LIMIT = 100_000
DISK_SPACE = 70_000_000
UPDATE_SIZE = 30_000_000

ROOT = r"/"
PARENT = r"\.\."

NAME = r"\w+"
EXT = r"\.\w{3}"
SIZE = r"\d+"

CD = re.compile(f"\$ cd ({ROOT}|{PARENT}|{NAME})")
LS = re.compile(f"\$ ls")
DIR = re.compile(f"dir ({NAME})")
FILE = re.compile(f"({SIZE}) ({NAME}({EXT})?)")


def read_input():
    lines = []
    while (True):
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    return lines


def parse_terminal(commands):

    def point(path, dirs):
        pointer = path["/"]
        for d in dirs[1:]:
            pointer = pointer[d]
        return pointer

    path = {"/": {}}
    dirs = []
    pointer = None

    for command in commands:
        cd = CD.fullmatch(command)
        ls = LS.fullmatch(command)
        d = DIR.fullmatch(command)
        f = FILE.fullmatch(command)

        if cd:
            name = cd.group(1)
            if name == "..":
                dirs.pop()
            else:
                dirs.append(name)
            pointer = point(path, dirs)
        if ls:
            continue
        if d:
            name = d.group(1)
            pointer[name] = {}
        if f:
            name = f.group(2)
            size = int(f.group(1))
            pointer[name] = size

    return path


def size(path):

    def _size(path, sizes):
        if not isinstance(path, dict):
            return (path, False)

        pairs = [_size(path[key], sizes) for key in path.keys()]
        sizes += [size for size, is_dir in pairs if is_dir]
        total_size = sum([size for size, _ in pairs])

        return (total_size, True)

    dir_sizes = []
    total_size, _ = _size(path, dir_sizes)
    return (total_size, dir_sizes)


def main(_):
    commands = read_input()
    file_system = parse_terminal(commands)

    used_space, dir_sizes = size(file_system)

    targets = [dir_size for dir_size in dir_sizes if dir_size <= SIZE_LIMIT]
    print(sum(targets))

    unused_space = DISK_SPACE - used_space
    needed_space = UPDATE_SIZE - unused_space
    targets = [dir_size for dir_size in dir_sizes if dir_size >= needed_space]
    print(min(targets))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
