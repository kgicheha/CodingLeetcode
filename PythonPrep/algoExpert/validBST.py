'''
Question Link:
https://www.algoexpert.io/questions/validate-bst

A node is said to be a valid BST node if and only if it satisfies the BST property:
    its value is strictly greater than the values of every node to its left
    its value is less than or equal to the values of every node to its right
'''

class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):

    minValue = float("-inf")
    maxValue = float("inf")

    currentNode = tree
    return validateBstHelper(currentNode, minValue, maxValue)

def validateBstHelper(currentNode, minValue, maxValue):

    if currentNode is None:
        return True

    if currentNode.value < minValue or currentNode.value >= maxValue:
        return False

    parentValue = currentNode.value

    leftChildCheck = validateBstHelper(currentNode.left, minValue, parentValue)
    rightChildCheck = validateBstHelper(currentNode.right, parentValue, maxValue)

    return leftChildCheck and rightChildCheck


# tree = BST(10)
# tree.left = BST(5)
# tree.left.left = BST(2)
# tree.left.right = BST(5)
# tree.left.left.left = BST(1)
# tree.right = BST(15)
# tree.right.left = BST(13)
# tree.right.right = BST(22)
# tree.right.left.right = BST(14)

tree = BST(20)
tree.left = BST(10)
tree.left.left = BST(5)
tree.left.right = BST(10)
tree.left.left.left = BST(1)
tree.right = BST(40)
tree.right.left = BST(30)
tree.right.right = BST(50)


print(validateBst(tree))



'''
A node is said to be a valid BST node if and only if it satisfies the BST property:
    its value is strictly greater than the values of every node to its left
    its value is less than or equal to the values of every node to its right

GIVEN:
    a tree

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
        this will check to ensure than the value of the left Child is less than the value of its parents' NodeValue

    using recursion check to see whether the right Child meets the criteria
        update the minimuValue to the current Nodes' value
        this will check to ensure that the value  right Child is greater than or equal to the value of its parents' Node

    return True if it successfully goes throught the entire tree.


RESULT:
    True if the given tree is valid
    False if the given tree is invalid

Time Complexity: O(n) --> have to traverse entire tree
Space Complexity: O(d) --> d represents the depth of the longest branch in the given tree
'''