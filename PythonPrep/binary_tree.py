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

    def printInorder(self, node, result = []):

        if node is not None:
            self.printInorder(node.leftChild, result)
            result.append(node.data)
            self.printInorder(node.rightChild, result)

        print(result)

    def printPreOrder(self, node, result = []):

        if node is not None:
            result.append(node.data)
            self.printPreOrder(node.leftChild, result)
            self.printPreOrder(node.rightChild, result)

        print(result)

    def printPostOrder(self, node, result = []):

        if node is not None:
            self.printPostOrder(node.leftChild, result)
            self.printPostOrder(node.rightChild, result)
            result.append(node.data)

        print(result)


bin_tree = binaryTree()
root = bin_tree.createNode(5)
bin_tree.insert(root, 1)
bin_tree.insert(root, 4)
bin_tree.insert(root, 3)
bin_tree.insert(root, 2)
# bin_tree.printInorder(root)
bin_tree.printPreOrder(root)
# bin_tree.printPostOrder(root)
