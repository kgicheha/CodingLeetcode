'''
Question Link:
https://www.algoexpert.io/questions/bst-construction
'''

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):

        currentNode = self

        while currentNode != None:

            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left

            if value > currentNode:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    def contains(self, value):

        currentNode = self

        while currentNode != None:

            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True

        return False

    def remove(self, value):
        return self


root  = BST.insert(1)
root.insert(2)


'''
INSERTION USING ITERATION
    initialize currentNode to self

    while True:

        if the given value is less to the currentNode.value:
            check to see if the left child is empty

            if the left child is empty:
                initialize the left child to the BST function with the given value as an argument

            else if the a left child does exist:
                traverse to the left child by setting the currentNode equal to the currentNode.left child

        else:
            check to see if right child is empty

            if the right child is empty:
                set the child equal to the value using the BST function and passing the value as its argument

            else if a right child does exist:
                move on to the right child then check the condition
                do this by setting the currentNode equal to its right child

    return self

#  Average Time Complexity --> O(log n) || Space Complexity --> O(1)
#  Worst Time Complexity --> O(n) || Space Complexity --> O(1)
'''

'''
CHECK TO SEE IF A BST CONTAINS A VALUE using ITERATION

    initialize currentNode to self

    while currentNode != None
        if given value < currentNode.value:
            search the left branch

        else if given value > currentNode.value:
            seearch the right branch

        else:
            return True meaning the Node has been found

    return False if the value is not found


#  Average Time Complexity --> O(log n) || Space Complexity --> O(1)
#  Worst Time Complexity --> O(n) || Space Complexity --> O(1)
'''

'''

'''