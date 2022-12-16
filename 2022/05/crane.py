class Command:

    pattern = r"move (\d+) from (\w+) to (\w+)"

    def __init__(self, origin, destination, amount=1):
        self.origin = origin
        self.destination = destination
        self.amount = amount


class Crane:

    def __init__(self, commands=[], enhanced=False):
        self._commands = commands
        self._enhanced = enhanced

    def _rearrange_single(self, stacks):
        for cmd in self._commands:
            for _ in range(cmd.amount):
                crate = stacks[cmd.origin].pop()
                stacks[cmd.destination].push(crate)

    def _rearrange_multiple(self, stacks):
        for cmd in self._commands:
            crates = []
            for _ in range(cmd.amount):
                crates.append(stacks[cmd.origin].pop())
            crates.reverse()
            for crate in crates:
                stacks[cmd.destination].push(crate)

    def rearrange(self, stacks):
        if self._enhanced:
            self._rearrange_multiple(stacks)
        else:
            self._rearrange_single(stacks)
