
'''
Question Link:
https://www.algoexpert.io/questions/branch-sums

'''

'''
GIVEN:
    root of a binary tree
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
    result = []
    sumHelper(root, result, currentSum = 0)

    return result

def sumHelper(node, result, currentSum):
    if node is None:
        return

    currentSum += node.value

    if node.left is None and node.right is None:
        result.append(currentSum)
        return

    sumHelper(node.left, result, currentSum)
    sumHelper(node.right, result, currentSum)



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