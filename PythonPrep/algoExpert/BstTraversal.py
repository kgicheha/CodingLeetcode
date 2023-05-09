'''
Question Link:
https://www.algoexpert.io/questions/bst-traversal
'''

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorderTraverse(tree, array):

    if tree is not None:
        inOrderTraverse(tree.leftChild, array)
        array.append(tree.data)
        inOrderTraverse(tree.rightChild, array)

tree = BST(10)
tree.left = BST(5)
tree.left.left = BST(2)
tree.left.right = BST(5)
tree.left.left.left = BST(1)
tree.right = BST(15)
tree.right.right = BST(22)


'''
GIVEN:
    1. empty array
    2. tree
STEPS:

    inorderTraversal
RESULTS:
    return the array with the tree
'''