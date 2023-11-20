def swapPairs(head):
    pass


'''
STEPS:
    while cur
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0


    def add(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head =  new_node
            self.length += 1
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        self.length += 1


    def printList(self):
        current_node =self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next





head = LinkedList()
newList.add(1)
newList.add(2)
newList.add(3)
newList.add(4)
print(newList.length)