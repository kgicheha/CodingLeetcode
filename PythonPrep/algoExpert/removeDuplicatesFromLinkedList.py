class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    return None


root = LinkedList(1)
root.next = LinkedList(4)
root.next.next = LinkedList(4)
root.next.next.next = LinkedList(5)
root.next.next.next.next = LinkedList(6)