class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next

    # ADDING AT THE END OF LIST
    def append(self, data):

            new_node = Node(data)

            if self.head == None:
                self.head = new_node
                return

            current = self.head
            while current.next != None:
                current = current.next

            current.next = new_node

    # ADDING AT THE BEGGING OF LIST
    def prepend(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        new_node.next = self.head
        self.head = new_node


    def reverseList(self):
        # if list is empty

        if self.head is None:
            return self.head

        current = self.head
        previous = None
        next = None

        while current != None:

            next = current.next
            current.next = previous
            previous = current
            current = next

        return previous






my_llist = LinkedList()
print(my_llist.append(5))
my_llist.append(3)
# my_llist.prepend(1)
my_llist.printList()
# my_llist.reverseList()
