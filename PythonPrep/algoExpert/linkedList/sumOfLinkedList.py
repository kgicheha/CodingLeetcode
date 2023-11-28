class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def unshift(self, val):

        newNode = ListNode(val)

        newNode.next = self.head
        self.head = newNode


    def print(self):
        if self.head is None:
            return None

        curNode = self.head
        while curNode:
            print(curNode.val)
            curNode = curNode.next


def sumLinkedList(l1, l2):

    l1Vals = ""
    l2Vals = ""

    curNode = l1

    while curNode:
        l1Vals += str(curNode.val)
        curNode = curNode.next

    curNode = l2

    while curNode:
        l2Vals += str(curNode.val)
        curNode = curNode.next

    result = str(int(l1Vals) + int(l2Vals))

    print(result)
    newLinkedList = LinkedList()
    for i in result:
        newLinkedList.unshift(int(i))

    newLinkedList.print()

if __name__ == "__main__":
    l1 = LinkedList()
    l1.unshift(3)
    l1.unshift(4)
    l1.unshift(2)
    l1.print()

    l2 =LinkedList()
    l2.unshift(4)
    l2.unshift(6)
    l2.unshift(5)
    l2.print()

    sumLinkedList(l1.head, l2.head)


