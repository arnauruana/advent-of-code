import sys


REG_VALUE = 1

BASE_CYCLE = 20
NEXT_CYCLE = 40

SPRITE_WIDTH = 3

CRT_WIDTH = 40
CRT_HEIGHT = 6

LIT_PIXEL = "#"
DARK_PIXEL = "."


def read_input():
    lines = []
    while (True):
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    return lines


def parse_input(program):

    def parse(inst):
        if len(inst) > 1:
            return (
                str(inst[0]),
                int(inst[1])
            )
        return [str(inst[0])]

    program = [instruction.split() for instruction in program]
    program = [parse(instruction) for instruction in program]
    return program


def init_crt():
    w, h = CRT_WIDTH, CRT_HEIGHT
    return [[DARK_PIXEL for _ in range(w)] for _ in range(h)]


def handle_cycle(cycle, register, strengths, crt):

    def are_overlapping(pixel, sprite):
        return abs(pixel%CRT_WIDTH - sprite) <= SPRITE_WIDTH // 2

    def signal_strength(cycle, register):
        if cycle % NEXT_CYCLE == BASE_CYCLE:
            return cycle * register
        return False

    if are_overlapping(cycle, register):
        crt[cycle//40][cycle%40] = "#"

    cycle += 1

    if strength := signal_strength(cycle, register):
        strengths.append(strength)

    return cycle


def execute(program, crt):
    cycle = 0
    register = REG_VALUE

    strengths = []
    for instruction in program:
        cycle = handle_cycle(cycle, register, strengths, crt)
        if instruction[0] == "addx":
            cycle = handle_cycle(cycle, register, strengths, crt)
            register += instruction[1]

    return strengths


def display(crt):
    crt = ["".join(row) for row in crt]
    return "\n".join(crt)


def main(_):
    program = read_input()
    program = parse_input(program)

    crt = init_crt()
    signal_strengths = execute(program, crt)

    print(sum(signal_strengths))
    print(display(crt))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
