from collections import deque


class Queue(deque):

    def size(self):
        return len(self)

    def empty(self):
        return self.size() == 0

    def front(self):
        if self.empty():
            return None
        return self[0]

    def push(self, element):
        return self.append(element)

    def pop(self):
        return self.popleft()
