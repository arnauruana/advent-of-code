import sys


NUM_KNOTS = 10


def read_input():
    lines = []
    while (True):
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    return lines


def parse_input(cmds):
    cmds = [cmd.split() for cmd in cmds]
    cmds = [(direction, int(steps)) for direction, steps in cmds]
    return cmds


def are_touching(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail

    dist_x = abs(head_x - tail_x)
    dist_y = abs(head_y - tail_y)

    return max(dist_x, dist_y) <= 1


def move(direction, head):
    match direction:
        case "L":
            incr = (0, -1)
        case "R":
            incr = (0, 1)
        case "U":
            incr = (1, 0)
        case "D":
            incr = (-1, 0)
        case _:
            raise ValueError("direction ≠ {'L'|'R'|'U'|'D'}")

    head_x, head_y = head
    incr_x, incr_y = incr

    return (
        head_x + incr_x,
        head_y + incr_y
    )


def follow(head, tail):
    if are_touching(head, tail):
        return tail

    head_x, head_y = head
    tail_x, tail_y = tail

    dist_x = head_x - tail_x
    dist_y = head_y - tail_y

    incr_x = max(-1, min(dist_x, 1))
    incr_y = max(-1, min(dist_y, 1))

    return (
        tail_x + incr_x,
        tail_y + incr_y
    )


def simulate(cmds, knots=2):
    rope = [(0, 0) for _ in range(knots)]

    positions = [rope[-1]]
    for cmd in cmds:
        direction, steps = cmd
        for _ in range(steps):
            rope[0] = move(direction, rope[0])
            for knot in range(1, knots):
                rope[knot] = follow(rope[knot-1], rope[knot])
            positions.append(rope[-1])

    return positions


def main(_):
    cmds = read_input()
    cmds = parse_input(cmds)

    tail_steps = simulate(cmds)
    print(len(set(tail_steps)))

    tail_steps = simulate(cmds, NUM_KNOTS)
    print(len(set(tail_steps)))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
