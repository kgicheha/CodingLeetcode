'''
Question Link:
https://www.algoexpert.io/questions/bst-traversal
'''

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inOrderTraverse(tree, array):

    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)

    return array

def preOrderTraversal(tree, array):

    if tree is not None:
        array.append(tree.value)
        preOrderTraversal(tree.left, array)
        preOrderTraversal(tree.right, array)

    return array


def postOrderTraversal(tree, array):

    if tree is not None:
        postOrderTraversal(tree.left, array)
        postOrderTraversal(tree.right, array)
        array.append(tree.value)

    return array


tree = BST(10)
tree.left = BST(5)
tree.left.left = BST(2)
tree.left.right = BST(5)
tree.left.left.left = BST(1)
tree.right = BST(15)
tree.right.right = BST(22)

print("inOrderResult", inOrderTraverse(tree, array = []))
print("preOrderResult", preOrderTraversal(tree, array = []))
print("postOrderResult", postOrderTraversal(tree, array = []))


'''
GIVEN:
    1. empty array
    2. tree
STEPS:

    inorderTraversal
RESULTS:
    return the array with the tree
'''