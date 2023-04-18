'''
Question Link:
https://www.algoexpert.io/questions/node-depths
'''

'''
GIVEN:
    takes in a binary tree
STEPS:
    initialize depthSum to 0

    Base Case:
    if node is None:
        return 0

    return the depthSum +
        recursively call if for the left child and increment depthSum by 1 +
            recursively call if for the right child and increment depthSum by 1

RESULT:
    return the sum of its nodes' depth
'''

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root, depthSum = 0):
    if root is None:
        return 0

    return depthSum + nodeDepths(root.left, depthSum + 1) + nodeDepths(root.right, depthSum + 1)


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)

print(nodeDepths(root))