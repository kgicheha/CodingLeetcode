class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 1

    def display(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next

    # GET NODE FROM A PARTICULAR INDEX
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        current = self.head

        i = 0
        while i < index:
            current = current.next
            i += 1
        return current

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

        self.length += 1

    # ADDING AT THE BEGGING OF LIST
    def prepend(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        new_node.next = self.head
        self.head = new_node

        self.length += 1


    # ADDING INSIDE THE LIST
    def insert(self, index, data):

        if index == 0:
            return self.prepend(data)
        if index == self.length - 1:
            return self.append(data)

        if index < 0 or index >= self.length:
            return None

        new_node = Node(data)

        current = self.get(index - 1)

        new_node.next = current.next

        current.next = new_node

        self.length += 1

        return True

    # ADDING IN THE MIDDLE OF A LINKED LIST
    def insert_in_middle(self, data):

        new_node = Node(data)

        # get the length of list
        list_length = 0
        current = self.head

        while current:
            list_length += 1
            current = current.next

        # print("Length of List",list_length)

        # get the middle index then traverse to the middle
        middle = list_length // 2

        current = self.head

        counter = 0
        while current:
            if counter == middle - 1 :
                new_node.next = current.next
                current.next = new_node

            current = current.next
            counter += 1

        self.length += 1


    # CHANGING A VALUE FROM A PARTICULAR INDEX
    def set(self, index, data):
        current = self.get(index)

        if current:
            current.data = data
            return True

        return False

    # DELETION AT THE BEGINNING OF LIST
    def shift(self):
        if self.head == None:
            return None

        current = self.head
        self.head = self.head.next
        current.next = None
        self.length -= 1

        return current.data



    # DELETION AT THE END OF LIST
    def pop(self):
        if self.head == None:
            return None

        current = self.head
        previous = self.head

        while current.next:
            previous = current
            current = current.next

        previous.next = None

        self.length -= 1

        if self.length == 0:
            self.head = None

        return current.data

    # REMOVING NODE FROM A PARTICULAR INDEX
    def remove(self, index):
        if index == 0:
            return self.shift()
        if index == self.length - 1:
            return self.pop()
        if index < 0 or index >= self.length:
            return None

        previous = self.get(index - 1)

        current = previous.next

        previous.next = previous.next.next
        current.next = None

        self.length -= 1

        return current.data



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
my_llist.append(1)
my_llist.append(2)
my_llist.append(3)
my_llist.append(4)

# my_llist.prepend(100)
# my_llist.insert(2, 300)
my_llist.display()
# my_llist.set(3, 500)
my_llist.remove(2)
my_llist.display()

# my_llist.printList()
# print("Removed item",my_llist.remove(1))
# my_llist.printList()
# my_llist.reverseList()
