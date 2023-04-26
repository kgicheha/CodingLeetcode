'''
Question Link:
https://www.algoexpert.io/questions/middle-node
'''

'''
GIVEN:
    a linked list with AT LEAST one node
STEPS:
RESULT:
    return the middle node of the linked list

'''
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def middleNode(linkedList):
    return None

root = LinkedList(2)
root.next = LinkedList(7)
root.next.next = LinkedList(3)
root.next.next.next = LinkedList(5)

print(middleNode(root))