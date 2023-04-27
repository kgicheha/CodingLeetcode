'''
Question Link:
https://www.algoexpert.io/questions/depth-first-search

DEPTH FIRST SEARCH:
    Traverse a tree from LEFT to RIGHT
'''

'''
GIVEN:
    1. a node class
    2. empty array
STEPS:

    add the name of the node to the given empty array

    call the function RECURSIVELY each child and pass in the given array as the argument.

    return the given array

RESULTS:
    return the input array after storing all the nodes' names


Time Complexity --> O(v + e) --> v represenents the number of vertices or nodes in the graph
                    --> e represents the edges or the interconnected lines
Space Complexity --> O(v) --> represent the number of vertices in the tree
'''

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):

        array.append(self.name)

        for child in self.children:

                child.depthFirstChild(array)

        return array






root = Node("A")
child1 = "B"
child2 = "C"
child3 = "D"
root.addChild(child1)
root.addChild(child2)
root.addChild(child3)

print(root.depthFirstSearch)