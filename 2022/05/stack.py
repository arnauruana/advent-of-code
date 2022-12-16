from collections import deque


class Stack(deque):

    def size(self):
        return len(self)

    def empty(self):
        return self.size() == 0

    def top(self):
        if self.empty():
            return None
        return self[-1]

    def push(self, element):
        return self.append(element)

    def pop(self):
        return super().pop()
