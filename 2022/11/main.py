import math
import sys
from copy import deepcopy as clone

from monkey import Monkey


def read_input():
    lines = input()
    while (True):
        try:
            lines += "\n" + input()
        except EOFError:
            break
    return lines


def parse_input(notes):
    notes = Monkey.PATTERN.finditer(notes)
    notes = [note.groupdict() for note in notes]
    return notes


def parse_monkeys(notes):

    def parse_monkey(note):

        def parse_items(items):
            items = items.split(", ")
            items = [int(item) for item in items]
            return items

        def parse_operation(op):
            return op

        def parse_condition(cond):
            cond = f"item % {cond} == 0"
            return cond

        def parse_throwing(throw_to):
            throw_to = int(throw_to)
            return throw_to

        return Monkey(
            items=parse_items(note["items"]),
            operation=parse_operation(note["op"]),
            condition=parse_condition(note["cond"]),
            true=parse_throwing(note["true"]),
            false=parse_throwing(note["false"])
        )

    monkeys = [parse_monkey(note) for note in notes]
    divs_by = [int(note["cond"]) for note in notes]
    return (monkeys, math.lcm(*divs_by))


def monkey_business(monkeys, rounds, lcm=None):

    def top(n, elements):
        elements.sort(reverse=True)
        return elements[:n]

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.turn(monkeys, lcm)

    inspections = [monkey.inspections for monkey in monkeys]
    return math.prod(top(2, inspections))


def main(_):
    notes = read_input()
    notes = parse_input(notes)

    monkeys, lcm = parse_monkeys(notes)

    print(monkey_business(clone(monkeys), 20))
    print(monkey_business(clone(monkeys), 10000, lcm))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
