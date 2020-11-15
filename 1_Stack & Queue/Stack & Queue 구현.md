# Stack & Queue 구현 [Python3]

### Prob.

1. **Stack** 구현
2. **Queue** 구현

<br/>



### Sol.

* Stack과 Queue 각각 **Class 형태**로 구현
* `add()` : Stack 또는 Queue에 데이터 삽입
* `pop()` : Stack 또는 Queue에서 데이터 가져오기
* `look()` : Stack 또는 Queue에서 다음에 나올 데이터 보기

<br/>

<br/>

가장 기본적인 자료구조라고 할 수 있는 **Stack & Queue** 를 `Python3` 로 간단하게 구현해보았다.

Class 형태로 구현해 보았으며, 각 클래스는 `add()`, `pop()`, `look()`, 이렇게 위의 **Sol.**에서 설명한 것과 같이 각각 데이터의 삽입, 가져오기(제거), 조회 기능을 갖도록 구현해보았다.

<br/>

먼저, **Stack**의 코드이다.

```python
class Stack:
    _stack = []

    def add(self, data):
        self._stack.append(data)

    def pop(self):
        return self._stack.pop()

    def look(self):
        return self._stack[-1]
```

**Stack**의 경우 `LIFO(Last In First Out)` 방식의 자료구조로써, 가장 최근(마지막)에 들어간 데이터를 가장 먼저 반환하는 자료구조이다.

<br/>

다음으로, **Queue**의 코드이다.

```python
class Queue:
    _queue = []

    def add(self, data):
        self._queue.append(data)

    def pop(self):
        return self._queue.pop(0)

    def look(self):
        return self._queue[0]
```

**Queue**의 경우 `FIFO(First In First Out)` 방식의 자료구조로써, 가장 먼저 들어간 데이터를 가장 먼저 반환하는, 즉 **데이터가 들어온 순서대로 나가는** 자료구조이다.

<br/>

아래는 Test Code를 포함한 전체 소스 코드이다.

각 자료구조에 `1` 과 `2` 를 넣고 반환을 요청할 경우, 어떠한 값이 반환되는지 보는 테스트 코드로써, **Stack & Queue**의 차이점을 확인하는 데 있어 가장 기본이 되는 코드이다.

```python
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

```

