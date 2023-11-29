class BST:
    def __init__(self, data):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

        return self

    def getMinVal(self):
        if self.left is None:
            return self.value
        else:
            self.left.getMinVal()

    def search(self, value):
        if self.value == value:
            return self
        elif value < self.value:
            self.left.search(value)
        else:
            self.right.search(value)

'''
INSERT method

    1. if data is < than the current Nodes' value:
        check to see if left child is empty or not

        if left child is empty:
            set the new value as the left child
        else:
            recursively call the INSERT method on the left child with the new value

    if the data >= the current Nodes value:
        check to see if right child is empty or not

        if the right child is empty:
            set the new value as the right child
        else:
            recursively call the INSERT method on the right child with the new value



GET MINIMUM VALUE
    if the currentNode doesnt have a left child:
        return this node's value
    else:
        recursively call the method on the left child

'''