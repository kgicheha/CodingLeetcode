
'''
Question Link:
https://www.algoexpert.io/questions/branch-sums

'''

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    print(root)


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