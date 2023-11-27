class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def contains(self, value):
        if self.head is None:
            return None

        curNode = self.head

        while curNode:
            if curNode.data == value:
                return True
            curNode = curNode.next

        return False

    def setHead(self,node):
        newNode = Node(node)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.size += 1
            return


l1 = LinkedList()
l1.setHead(4)
print(l1.contains(4))



