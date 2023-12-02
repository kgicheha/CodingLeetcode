class TreeNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insert(self, value):

        if value == self.value:
            return
        elif value < self.value:
            if self.leftChild is None:
                self.leftChild = TreeNode(value)
            else:
                return self.leftChild.insert(value)

        else:
            if self.rightChild is None:
                self.rightChild = TreeNode(value)
            else:
                return self.rightChild.insert(value)

        return

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

    # used for creating a copy of the tree
    def preOrderTraversal(self):
        print(self.value)

        if self.leftChild:
            self.leftChild.preOrderTraversal()

        if self.rightChild:
            self.rightChild.preOrderTraversal()

    # return the non-decreasing order
    def inOrderTraversal(self):
        if self.leftChild:
            self.leftChild.inOrderTraversal()
        print(self.value)
        if self.rightChild:
            self.rightChild.inOrderTraversal()

    # used for tree deletion
    def postOrderTraversal(self):
        if self.leftChild:
            self.leftChild.postOrderTraversal()

        if self.rightChild:
            self.rightChild.postOrderTraversal()

        print(self.value)

root = TreeNode(4)

root.insert(2)
root.insert(5)
root.insert(1)
root.insert(3)
root.insert(6)
root.insert(7)
root.insert(4)

root.postOrderTraversal()
print(root.find(7))
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