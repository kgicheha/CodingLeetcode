
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
            self.head = new_node
            self.length += 1
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        self.length += 1

    def reverseList(self):

        if self.head is None:
            print(head)

        if self.head.next is None:
            return head

        new_head = self.reverseList(self.head.next)

        self.head.next.next = head

        self.head.next = None

        return new_head


head = LinkedList()
head.reverseList()
# head.add("A")
# head.add("B")
# head.add("C")
# print(head.length)

# head.reverseList()