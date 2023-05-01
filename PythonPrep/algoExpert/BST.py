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

        while True:

            if value < currentNode:
                if currentNode.left is None:
                    currentNode = BST(value)

                else:
                    currentNode = currentNode.left


            if value > currentNode:
                if currentNode.right is None:
                    currentNode = BST(value)
                else:
                    currentNode = currentNode.right
        return self

    def contains(self, value):
        print(value)

    def remove(self, value):
        return self


root  = BST.insert(1)
root.insert(2)


'''
INSERTION USING ITERATION

    initialize currentNode to self

    while True:

        if the given value is less to the currentNode:
            check to see if the left child is empty

            if the left child is empty:

'''
