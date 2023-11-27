class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


    def get(self,index):
        if index < 0 or index >= self.size:
            return -1

        dummyHead = self.head

        for i in range(index):
            dummyHead = dummyHead.next

        return dummyHead.data


    def addAtHead(self,data):
        newNode = Node(data)

        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def addAtTail(self, data):
        newNode = Node(data)

        currentNode = self.head

        while currentNode.next:
            currentNode = currentNode.next

        currentNode.next = newNode
        self.size += 1

    def addAtIndex(self, data):
        if index > self.size:
            return

        newNode = Node(data)

        currentNode = self.head

        if index <= 0:
            newNode.next = currentNode
            self.head = newNode

        else:
            for i in range(index - 1):
                currentNode = currentNode.next
            newNode.next = currentNode.next
            currentNode.next = newNode

        self.size += 1


    def deleteAtIndex(self,index):
        if index < 0    or index >= self.index:
            return

        currentNode = self.head

        if index == 0:
            self.head = self.head.next

        else:
            for i in range(index -  1):
                currentNode = currentNode.next

            currentNode.next = currentNode.next.next

        self.size -= 1


    def printList(self):
        dummyHead = self.head

        while dummyHead:
            print(dummyHead.data,end=" ")
            dummyHead = dummyHead.next


l1 = LinkedList()
l1.addAtHead(4)
l1.addAtHead(3)
l1.addAtHead(2)
l1.addAtHead(1)
l1.addAtTail("Tail")

print(l1.get(4))
l1.printList()