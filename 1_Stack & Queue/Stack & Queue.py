# 구현 - Stack & Queue

class Stack:
    _stack = []

    def add(self, data):
        self._stack.append(data)

    def pop(self):
        return self._stack.pop()

    def look(self):
        return self._stack[-1]


class Queue:
    _queue = []

    def add(self, data):
        self._queue.append(data)

    def pop(self):
        return self._queue.pop(0)

    def look(self):
        return self._queue[0]


def test():
    # Stack
    stack = Stack()
    stack.add(1)
    stack.add(2)
    resStack = stack.pop()
    print('Result(Stack) >> {}'.format(resStack))

    # Queue
    queue = Queue()
    queue.add(1)
    queue.add(2)
    resQueue = queue.pop()
    print('Result(Queue) >> {}'.format(resQueue))


if __name__ == '__main__':
    test()
