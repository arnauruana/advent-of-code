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


def extract_ranges(pair):
    range1, range2 = pair.split(',')
    range1_min, range1_max = range1.split('-')
    range2_min, range2_max = range2.split('-')
    return (
        (int(range1_min), int(range1_max)),
        (int(range2_min), int(range2_max))
    )


def is_contained(inner, outer):
    inner_min, inner_max = inner
    outer_min, outer_max = outer
    return (
        inner_min >= outer_min
        and inner_max <= outer_max
    )


def are_contained(range1, range2):
    return (
        is_contained(range1, range2)
        or is_contained(range2, range1)
    )


def are_overlapping(range1, range2):
    min1, max1 = range1
    min2, max2 = range2
    return max(min1, min2) <= min(max1, max2)


def main(_):
    pairs = read_input()
    pairs = [extract_ranges(pair) for pair in pairs]

    containments = [are_contained(range1, range2) for range1, range2 in pairs]
    print(sum(containments))

    overlaps = [are_overlapping(range1, range2) for range1, range2 in pairs]
    print(sum(overlaps))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
