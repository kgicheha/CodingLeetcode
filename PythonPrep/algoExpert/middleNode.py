'''
Question Link:
https://www.algoexpert.io/questions/middle-node
'''

'''
GIVEN:
    a linked list with AT LEAST one node
STEPS:
    traverse linked list to get the length of the list

    initialize middleIndex to length // 2

    reset linkedList back to original

    traverse linked list untile you get to the middle index
        return value of the middle node
RESULT:
    return the middle node of the linked list

'''
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def middleNode(linkedList):

    length = 0
    temp = linkedList

    while temp:
        length += 1
        temp = temp.next

    middleIndex = length // 2

    currentIndex = 0

    temp2 = linkedList

    while currentIndex != middleIndex:
        temp2 = temp2.next
        currentIndex += 1

    return temp2


root = LinkedList(2)
root.next = LinkedList(7)
root.next.next = LinkedList(3)
root.next.next.next = LinkedList(5)

print(middleNode(root))