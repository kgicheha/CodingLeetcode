'''
Question Link:
https://www.algoexpert.io/questions/bst-construction
'''

'''
GIVEN:
STEPS:
RESULT:
'''

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):

        # if tree is empty
        if self.value is None:
            self.value = value

        # if given value is equal to value
        if self.value == value:
            return

        # if current value is less than given value
        elif value < self.value:
            self.left = self.insert(self, self.left, value)

        # if current value is more than given value
        elif value > self.value:
            self.insert(self, self.right, value)

        return self

    def contains(self, value):
        print(value)

    def remove(self, value):
        return self


root  = BST.insert(1)
root.insert(2)


