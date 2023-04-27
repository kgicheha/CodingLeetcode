'''
Question Link:
https://www.algoexpert.io/questions/breadth-first-search


BREADTH FIRST SEARCH:

'''
'''
GIVEN:
STEPS:
RESULTS:

'''

class Node:
    def __init__(self, name):
        self.name = name
        self.children =[]

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        pass


