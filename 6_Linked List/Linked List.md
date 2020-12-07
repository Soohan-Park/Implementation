# Linked List 구현 [Python3]

### Prob.

1. **Linked List** 구현

<br/>

### Sol.

* `Linked List`라는 클래스 형태로 구현하였으며, `값` &middot; `왼쪽 노드` &middot; `오른쪽 노드`, 총 3개의 속성을 가짐.
* (주의) 서로 다른 두 노드를 연결 시, 양쪽 모두에 연결된 정보가 기록되도록 해야 함.

<br/>
<br/>

자료구조 구현 중, 리스트를 구현할 때 `ArrayList` 다음으로 가장 많이 나오는 리스트, `Linked List`.

이번 글에선, 이 `Linked List`를 한 번 `Python`으로 구현해보고자 한다.

<br/>

먼저, `Linked List`의 구현된 노드 클래스는 아래와 같다.

<br/>

```python
class LinkedList:
    value = None
    leftNode = None
    rightNode = None

    def __init__(self, value=None, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

    def print(self):
        print( 'VALUE: {}\n'
               'LNODE: {}\n'
               'RNODE: {}\n'.format(self.value, self.leftNode, self.rightNode))

    def setValue(self, value):
        self.value = value

    def setLeftNode(self, leftNode):
        self.leftNode = leftNode
        leftNode.rightNode = self  # 연결되는 반대편 쪽에도!

    def setRightNode(self, rightNode):
        self.rightNode = rightNode
        rightNode.leftNode = self  # 연결되는 반대편 쪽에도!
```

<br/>

위 **Sol.**에서 언급했던 것과 같이, 해당 노드 클래스는 총 3개의 멤버를 가지고 있으며, 각각의 변수는 아래와 같다.

> * **value : **해당 노드가 가지고 있는 값
> * **leftNode : **해당 노드의 **왼쪽**에 있는 값
> * **rightNode : **해당 노드의 **오른쪽**에 있는 값



또한, `__init__` 메서드의 경우 인스턴스가 생성될 시 초기화를 담당하는 **생성자**의 역할을 수행하며,  
*(여기선 매개변수로 값 또는 좌&middot;우의 노드가 주어질 경우 그에 맞게 설정되도록 구현하였다.)*

`setValue()` &middot; `setLeftNode()` &middot; `setRightNode()` 는 각 멤버 변수에 값을 설정하는 **Setter**로써의 역할을 수행한다.

*(이 때, 중요한 점은 한 노드에서 다른 노드를 좌&middot;우로 연결시켜줄 때  **연결되어지는(?) 노드에도 그 정보가 입력이 되어야 한다는 것**이다!)*

<br/>

예전에 `C`로 `Linked List`를 구현할 때는 뭔가 코드가 더 복잡하고 길었던 것 같았는데...

`Python`이라 그런것인지~~*(실력이 늘은건 아닌거 같은ㄷ...)*~~ 생각보다 구현하는 데 있어, 생각보다 코드가 간결하게 나온 것 같다.

아래의 코드는 test 코드를 포함한 소스 코드 전문이다.

<br/>

```python
class LinkedList:
    value = None
    leftNode = None
    rightNode = None

    def __init__(self, value=None, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

    def print(self):
        print( 'VALUE: {}\n'
               'LNODE: {}\n'
               'RNODE: {}\n'.format(self.value, self.leftNode, self.rightNode))

    def setValue(self, value):
        self.value = value

    def setLeftNode(self, leftNode):
        self.leftNode = leftNode
        leftNode.rightNode = self  # 연결되는 반대편 쪽에도!

    def setRightNode(self, rightNode):
        self.rightNode = rightNode
        rightNode.leftNode = self  # 연결되는 반대편 쪽에도!


def test():
    Node_1 = LinkedList(value=10)
    Node_2 = LinkedList(value=20)
    Node_3 = LinkedList(value=30)

    print('=========================================================')
    print('<<CHECK NODEs ID>>\n'
          'Node_1: {}\n'
          'Node_2: {}\n'
          'Node_3: {}'.format(Node_1, Node_2, Node_3))
    print('=========================================================\n')

    # Set Node
    Node_2.setLeftNode(Node_1)
    Node_2.setRightNode(Node_3)

    Node_1.print()
    Node_2.print()
    Node_3.print()


if __name__ == '__main__':
    test()

```
