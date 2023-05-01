'''
Question Link:
https://www.algoexpert.io/questions/remove-duplicates-from-linked-list
'''

'''
GIVEN:
    the head of the linked list
STEPS:
    initialize currentNode to the given head

    traverse linked list:
        initialize variable that finds the next distict value in the list
            set it equal to currentNode.next to begin with

        traverse the rest of the linked list:
            if the nextDistinct Node is not None AND the nextDistinctNode.value == currentNode.value
                this means you have a duplicate, so move on to the next Node in the list until you find a value thats different from your currentNode value

            once you find a distict Value, set the currentNode to point to that Node
                this will remove all the nodes between the current Node and the Node with the distinct value

            then set the currentNode equal to the Distict Node

    return the given head of the linked list

RESULTS:
    return the modified linked list still sorted
'''
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):

    currentNode = linkedList

    while currentNode != None:
        nextDistinctNode = currentNode.next

        while nextDistinctNode != None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next

        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode

    return linkedList


root = LinkedList(1)
root.next = LinkedList(4)
root.next.next = LinkedList(4)
root.next.next.next = LinkedList(5)
root.next.next.next.next = LinkedList(6)

print(removeDuplicatesFromLinkedList(root))