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
