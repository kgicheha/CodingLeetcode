def minHeightBst(array):
    pass

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)



'''
GIVEN:
    non-empty sorted array of distinct integers
STEPS:

    if len of array == 1:
        return the only element in the array


RESULTS:
    return the root of the BST

'''