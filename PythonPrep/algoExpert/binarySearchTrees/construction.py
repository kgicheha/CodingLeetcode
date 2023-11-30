class BST:
    def __init__(self, data):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insert(self, value):
        if value < self.value:
            if self.leftChild is None:
                self.leftChild = BST(value)
            else:
                self.leftChild.insert(value)

        else:
            if self.rightChild is None:
                self.rightChild = BST(value)
            else:
                self.rightChild.insert(value)

        return self

    def getMinVal(self):
        if self.leftChild is None:
            return self.value
        else:
            self.leftChild.getMinVal()

    def find(self, value):

        if value < self.value:
            if self.leftChild is None:
                return False
            else:
                return self.leftChild.find(value)
        elif value > self.value:
            if self.rightChild is None:
                return False
            else:
                return self.rightChild.find(value)
        else:
            return True
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