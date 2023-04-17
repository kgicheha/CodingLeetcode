'''
Question Link:
https://www.algoexpert.io/questions/find-closest-value-in-bst
'''

'''
GIVEN:
    1. binary search tree
    2. target integer value
STEPS:
    initialize minimum absolute difference to 0
    initialize closest value to 0
    if target value is LESS than the value of the current node, go to the LEFT child
    elif target value is GREATER than the value of the current node, go to the RIGHT child
RESULT:
    the closest value to that target value contained in the BST

'''
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)



def findClosestValueInBstHelper(tree, target, closest):
    # print(tree)
    currentNodeValue = tree.value
    min_difference = float("inf")
    current_difference = abs(target - currentNodeValue)

    if tree is None:
        return closest
    if abs(min_difference) > current_difference:
        closest = tree.value
    elif target < currentNodeValue:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > currentNodeValue:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest




tree = BST(10)
tree.left = BST(5)
tree.left.left = BST(2)
tree.left.right = BST(5)
tree.left.left.left = BST(1)
tree.right = BST(15)
tree.right.right = BST(22)
tree.right.left = BST(13)
tree.right.left.right = BST(14)

target = 12
print(findClosestValueInBst(tree, target))