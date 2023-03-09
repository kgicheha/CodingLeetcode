class treeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # ADDING CHILDREN
    def insert(self, data):

        if data < self.data:
            if self.leftChild:
               self.leftChild.insert(data)
            else:
                self.leftChild = treeNode(data)
                return
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = treeNode(data)
                return


    def printInorder(self):

            # self.printInorder(self.leftChild)
        if self.leftChild:
            self.leftChild.printInorder()

        print(self.data)

            # self.printInorder(self.rightChild)
        if self.rightChild:
            self.rightChild.printInorder()

    def printPreOrder(self):

        print(self.data)

        if self.leftChild:
            self.leftChild.printPreOrder()

        if self.rightChild:
            self.rightChild.printPreOrder()

    def printPostOrder(self):

        if self.leftChild:
            self.leftChild.printPostOrder()

        if self.rightChild:
            self.rightChild.printPostOrder()

        print(self.data)

bin_tree = treeNode(1)
bin_tree.insert(2)
bin_tree.insert(3)
bin_tree.insert(4)
bin_tree.insert(5)
bin_tree.printInorder()
