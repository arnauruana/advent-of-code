import sys


def read_input():
    lines = []
    while (True):
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    return lines


def parse_forest(forest):
    forest = [[int(tree) for tree in trees] for trees in forest]
    return forest


def col(matrix, index):
    return [
        matrix[i][j]
        for i in range(len(matrix))
        for j in range(len(matrix[i]))
        if j == index
    ]


def is_visible(tree, forest):

    def is_visible_from(side, tree, forest):
        i, j = tree
        tree = forest[i][j]

        match side:
            case "left":
                trees = forest[i][:j]
            case "right":
                trees = forest[i][j+1:]
            case "top":
                trees = col(forest, j)[:i]
            case "bottom":
                trees = col(forest, j)[i+1:]
            case _:
                raise ValueError("side ≠ {'left'|'right'|'top'|'bottom'}")

        return max(trees, default=-1) < tree

    return (
        is_visible_from("left", tree, forest)
        or is_visible_from("right", tree, forest)
        or is_visible_from("top", tree, forest)
        or is_visible_from("bottom", tree, forest)
    )


def scenic_score(tree, forest):

    def scenic_score_towards(direction, tree, forest):
        i, j = tree
        height = forest[i][j]

        match direction:
            case "left":
                trees = forest[i][:j]
                trees.reverse()
            case "right":
                trees = forest[i][j+1:]
            case "up":
                trees = col(forest, j)[:i]
                trees.reverse()
            case "down":
                trees = col(forest, j)[i+1:]
            case _:
                raise ValueError("direction ≠ {'left'|'right'|'up'|'down'}")

        distance = 0
        for tree in trees:
            distance += 1
            if tree >= height:
                break
        return distance

    return (
        scenic_score_towards("left", tree, forest)
        * scenic_score_towards("right", tree, forest)
        * scenic_score_towards("up", tree, forest)
        * scenic_score_towards("down", tree, forest)
    )


def main(_):
    forest = read_input()
    forest = parse_forest(forest)

    visibilities = [
        is_visible((i, j), forest)
        for i in range(len(forest))
        for j in range(len(forest[i]))
    ]
    print(sum(visibilities))

    scenic_scores = [
        scenic_score((i, j), forest)
        for i in range(len(forest))
        for j in range(len(forest[i]))
    ]
    print(max(scenic_scores))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
