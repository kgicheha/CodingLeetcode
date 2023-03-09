class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class binaryTree:
    def createNode(self, data):
        return Node(data)

    # ADDING CHILDREN
    def insert(self,node, data):

        # if the tree is empty, create new Node
        if node is None:
            return self.createNode(data)

        # if the given data is less than the current node data
        if data < node.data:
            node.leftChild = self.insert(node.leftChild, data)

        # else if given data is more than the current node data
        else:
            node.rightChild = self.insert(node.rightChild, data)

        return node

    def printInorder(self, root):

        result = []

        if root is not None:
            self.printInorder(root.leftChild)
            result.append(self.data)
            self.printInorder(root.rightChild)

        print(result)

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


bin_tree = binaryTree()
root = bin_tree.createNode(1)
bin_tree.insert(root, 2)
bin_tree.insert(root, 3)
bin_tree.insert(root, 4)
bin_tree.insert(root, 5)
# bin_tree.printInorder()
