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

    def reverseList(self, head):
        # if list is empty

        if head is None:
            return head

        current = head
        previous = None
        next = None

        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous

    def append(self, data):
        # create new Node using the Node Class
        new_node = Node(data)

        # if list is empty, set the head to new node
        if self.head == None:
            head = new_node
            return

        # traverse node until you get to the last node
        # set the last node.next equal to new node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = new_node



my_llist = LinkedList()
my_llist.append = Node(5)
my_llist.append = Node(3)
my_llist.printList()