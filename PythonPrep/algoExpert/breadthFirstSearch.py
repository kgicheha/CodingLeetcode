'''
Question Link:
https://www.algoexpert.io/questions/breadth-first-search


BREADTH FIRST SEARCH:
    want to traverse the graph level by level
    returns

'''
'''
GIVEN:
STEPS:
    initialize a queue using a list data structure
        have the given root node as the first item in the list

    traverse the queue while its' length is more than 0:
        initialize the currrent node as the first item in the queue

        append the current Nodes' child to our given array

        for each child of the current Node:
            append it to the queue

    traverse through graph
    for each child:
        append it to the queue

    return the result array

RESULTS:
    return the result array

Time Complexity --> O(v + e) --> v represents the vertices or nodes in the graph
            e represents the edges or the interconnected lines

Spaces Complexity --> O(v) --> v represents the vertices
'''

class Node:
    def __init__(self, name):
        self.name = name
        self.children =[]

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            currentNode =queue.pop(0)

            array.append(currentNode.name)

            for child in currentNode.children:
                queue.append(child)

        return array


