import sys
from itertools import product as indexes

from queue import Queue


START = 'S'
END = 'E'
HEIGHT = {START: 'a', END: 'z'}

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

DELTAS = [RIGHT, DOWN, LEFT, UP]


def read_input():
    lines = []
    while (True):
        try:
            lines.append(list(input()))
        except EOFError:
            break
    return lines


def parse_input(mountain):
    rows = range(len(mountain))
    cols = range(len(mountain[0]))

    def locate(height):
        is_match = lambda ij: mountain[ij[0]][ij[1]] == height
        return filter(is_match, indexes(rows, cols))

    start = next(locate(START))
    end = next(locate(END))

    def replace(index, height):
        mountain[index[0]][index[1]] = height
        return mountain

    mountain = replace(start, HEIGHT[START])
    mountain = replace(end, HEIGHT[END])

    mountain = [[ord(char) for char in row] for row in mountain]

    return mountain, start, end


def children(matrix, parent):

    def valid(dest, orig):
        rows = range(len(matrix))
        cols = range(len(matrix[0]))

        def is_inside(pos):
            return (
                pos[0] in rows and
                pos[1] in cols
            )

        def valid_slope(orig, dest):
            orig_height = matrix[orig[0]][orig[1]]
            dest_height = matrix[dest[0]][dest[1]]

            slope = orig_height - dest_height
            return slope <= 1

        return (
            is_inside(dest) and
            valid_slope(orig, dest)
        )

    children = [(parent[0] + di, parent[1] + dj) for di, dj in DELTAS]
    children = [child for child in children if valid(child, parent)]
    return children


def shortest_path(mountain, start, end):

    def bfs(matrix, start, end):
        visited = {end: None}
        queue = Queue([end])
        while not queue.empty():
            parent = queue.pop()
            height = matrix[parent[0]][parent[1]]
            if start is None and height == ord(HEIGHT[START]):
                return (visited, parent)
            if parent == start:
                return (visited, start)
            for child in children(matrix, parent):
                if child not in visited:
                    queue.push(child)
                    visited[child] = parent
        return (None, None)

    span_tree, best_spot = bfs(mountain, start, end)

    def path(tree, start, end):
        if tree is None:
            return [start]
        path = [start]
        child = tree[start]
        while child != tree[end]:
            path.append(child)
            child = tree[child]
        return path

    return path(span_tree, best_spot, end)


def main(_):
    mountain = read_input()
    mountain, start, end = parse_input(mountain)

    steps = lambda path: len(path) - 1

    print(steps(shortest_path(mountain, start, end)))
    print(steps(shortest_path(mountain, None, end)))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
