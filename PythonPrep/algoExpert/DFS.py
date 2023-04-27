'''
Question Link:
https://www.algoexpert.io/questions/depth-first-search
'''

'''
GIVEN:
STEPS:
RESULTS:
'''

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):

        if len(array) <= 1:
            return self.name
        else:

        pass


root = Node("A")
root.addChild = ["B", "E", "F"]
print(root.children)