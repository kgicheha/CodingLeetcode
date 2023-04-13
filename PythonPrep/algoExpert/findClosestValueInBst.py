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
    print(tree)
    min_difference = 0
    closest_value = 0




