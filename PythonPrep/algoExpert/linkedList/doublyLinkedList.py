class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    # adding a Node at the end of the list
    def append(self, data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode

        self.length += 1


    # adding a node at the beginning of the list
    def unshift(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode

        self.length += 1
        return

    # removing a node at the end of the list
    def pop(self):
        if self.head is None:
            return None

        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            temp.previous = None


        self.length -= 1
        return temp


    # removing node from the beginning of the list
    def shift(self):
        if self.head is None:
            return None

        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
            temp.next = None


        self.length -= 1
        return temp

    # inserting New Node To A Particular Index
    def insert(self, index, data):
        if index == 0:
            return self.unshift(data)

        if index == self.length:
            return self.append(data)

        if index < 0 or index >= self.length:
            return None


        newNode = Node(data)

        previousNode = self.get(index - 1)
        nextNode = previousNode.next

        previousNode.next = newNode
        newNode.previous = previousNode
        newNode.next = nextNode
        nextNode.previous = newNode

        self.length += 1

        return True

    # Getting Node From A Particular Index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        currentNode = self.head

        if index < self.length // 2:
            i = 0
            while i < index:
                currentNode = currentNode.next
                i += 1

        else:
            currentNode = self.tail

            i = self.length - 1
            while i > index:
                currentNode = currentNode.previous
                i -= 1

        return currentNode

    def setValue(self, index, data):
        currentNode = self.get(index)

        if currentNode:
            currentNode.data = data
            return currentNode.data

        else:
            return False


    def remove(self, index):
        if index == 0:
            return self.shift()

        if index == self.length - 1:
            return self.pop()

        if index < 0 or index >= self.length:
            return None


        currentNode = self.get(index)

        currentNode.previous.next = currentNode.next
        currentNode.next.previous = currentNode.previous
        currentNode.next = None
        currentNode.previous = None

        self.length -= 1
        return currentNode.data


    # checks to see if a node exists in list
    def contains(self, value):
        if self.head is None:
            return None

        currentNode = self.head

        while currentNode:
            if currentNode.data == value:
                return True
            currentNode = currentNode.next

        return False


    # print from beginning to end
    def printList(self):
        if self.head is None:
            return

        currentNode = self.head

        while currentNode:
            print(currentNode.data, end=" ")
            currentNode = currentNode.next


    # print from end to beginning
    def printListInReverse(self):

        if self.tail is None:
            return

        currentNode = self.tail

        while currentNode:
            print(currentNode.data, end=" ")
            currentNode = currentNode.previous

l1 = DoublyLinkedList()
l1.unshift(4)
l1.unshift(3)
l1.unshift(2)
l1.unshift(1)
l1.insert(2, 5000)

l1.printList()
print("Current Length is", l1.length)
l1.remove(2)
l1.printList()
print("Current Length is", l1.length)

print(l1.contains(4))
print(l1.contains(400))
