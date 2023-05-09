'''
Question Link:
https://www.algoexpert.io/questions/validate-bst

A node is said to be a valid BST node if and only if it satisfies the BST property:
    its value is strictly greater than the values of every node to its left
    its value is less than or equal to the values of every node to its right
'''

'''
GIVEN:
    a tree
STEPS:
    initialize value to keep track of the parents' value

    if leftChild is not None:
        check to see if the parents value is GREATER than the leftChilds' value
    else if rightChild is None:
        check to see if the parents' value is less than the rightChild's value

        return True if it successfully goes through entire loop

    return False
RESULT:
    True if the given tree is valid
    False if the given tree is invalid
'''
class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):

    minValue = float("-inf")
    maxValue = float("inf")

    return validateBstHelper(tree, minValue, maxValue)

def validateBstHelper(tree, minValue, maxValue):

    if tree is None:
        return True

    if tree.value  < minValue or tree.value >= maxValue:
        return False

    leftChildCheck = validateBstHelper(tree.left, minValue, tree.value)
    rightChildCheck = validateBstHelper(tree.right, tree.value, maxValue)

    return leftChildCheck and rightChildCheck



'''
A node is said to be a valid BST node if and only if it satisfies the BST property:
    its value is strictly greater than the values of every node to its left
    its value is less than or equal to the values of every node to its right


STEPS:

    initialize minimum Value to equal lowest number possible
    initialize maximum value to equal the highest number possible

    create a helper function that traverses down the tree to see if each node meets the criteria of a valid BST
        The funtion takes in Node, the minValue, and maxValue

    if the Node is None: --> this is the Base Case
        return True

    if the value of the current Node is less than the minimum Value or if the value of the currentNode is >= the maxValue:
        this shows that the current Node doesn't meet the criteria
        so return False

    using recursion check to see whether the leftChild meets the criteria
        update the maximum Value to the current Nodes' value
        this will check to ensure than the value of the left Child is be greater than or equal to its parents' NodeValue

    using recursion check to see whether the right Child meets the criteria
        update the minimuValue to the current Nodes' value
        this will check to ensure that the value  right Child is not less than the value of its parents' Node

    return True if it successfully goes throught the entire tree.


'''