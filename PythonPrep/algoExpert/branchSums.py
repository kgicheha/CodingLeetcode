
'''
Question Link:
https://www.algoexpert.io/questions/branch-sums

'''

'''
GIVEN:
    root of a binary tre
STEPS:
    traverse through each branch

RESULT:
    return an array of the sum of all the nodes in the binary tree branch
'''

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):

    return sumHelper(root, result = [])

def sumHelper(root, result):

    while root is not None:
        sumHelper(root.left, result)
        print(root.value)



root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)
root.left.right.left = BinaryTree(10)

root.right = BinaryTree(3)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)


print(branchSums(root))