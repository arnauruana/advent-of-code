import re
import sys
from copy import deepcopy as clone
from itertools import zip_longest

from crane import Command, Crane
from stack import Stack


def read_input():
    lines = []
    while (True):
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break

    split = lines.index('')
    return (
        lines[:split],
        lines[split+1:]
    )


def parse_stacks(stacks):
    stacks = [crates[1::4] for crates in stacks]
    stacks = zip_longest(*stacks[::-1], fillvalue=' ')
    stacks = map(lambda ls: (ls[0], ls[1:]), stacks)
    stacks = [(name, [crate for crate in crates if not crate.isspace()])
              for name, crates in stacks]
    stacks = {name: Stack(crates) for name, crates in stacks}
    return stacks


def parse_commands(commands):
    commands = [re.match(Command.pattern, command).groups()
                for command in commands]
    commands = [Command(orig, dest, int(amnt))
                for amnt, orig, dest in commands]
    return commands


def main(_):
    stacks, commands = read_input()
    stacks = parse_stacks(stacks)
    commands = parse_commands(commands)

    stacks_ = stacks

    stacks = clone(stacks_)
    crate_mover_9000 = Crane(commands)
    crate_mover_9000.rearrange(stacks)
    print(''.join([stack.top() for stack in stacks.values()]))

    stacks = clone(stacks_)
    crate_mover_9001 = Crane(commands, enhanced=True)
    crate_mover_9001.rearrange(stacks)
    print(''.join([stack.top() for stack in stacks.values()]))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
