import re
from collections import deque


PATTERN_ = r"""Monkey \d+:
  Starting items: (?P<items>.+)
  Operation: new = (?P<op>.+)
  Test: divisible by (?P<cond>\d+)
    If true: throw to monkey (?P<true>\d+)
    If false: throw to monkey (?P<false>\d+)"""


class Monkey:

    BORING_FACTOR = 3
    PATTERN = re.compile(PATTERN_)

    def __init__(self, items, operation, condition, true, false):
        self._items = deque(items)
        self._operation = operation
        self._condition = condition
        self._true = true
        self._false = false
        self._inspections = 0

    def empty(self):
        return len(self._items) == 0

    def inspect(self, lcm=None):
        old = self._items.popleft()
        self._inspections += 1

        new = eval(self._operation)
        if lcm is None:
            new //= Monkey.BORING_FACTOR
        else:
            new %= lcm
        return new

    def throw(self, item, monkeys):
        receiver = self._true if eval(self._condition) else self._false
        monkeys[receiver].catch(item)

    def turn(self, monkeys, lcm=None):
        while not self.empty():
            item = self.inspect(lcm)
            self.throw(item, monkeys)

    def catch(self, item):
        self._items.append(item)

    @property
    def inspections(self):
        return self._inspections
