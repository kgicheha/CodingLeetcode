class MinStack():
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)

        if self.minStack:
            minVal = min(val, self.minStack[-1])
            self.minStack.append(minVal)
        else:
            self.minStack.append(val)

    def pop(self):
        if len(self.stack) == 0:
            return "Stack is Empty"

        else:
            self.stack.pop()
            self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

    def printStack(self):
        print("Stack", self.stack)
        print("Min Value",self.stack)

sampleStack = MinStack()

sampleStack.push(4)
sampleStack.push(3)
sampleStack.push(1)
sampleStack.printStack()
sampleStack.pop()
sampleStack.printStack()
sampleStack.top()

'''
Link: https://leetcode.com/problems/min-stack/
'''

'''
STEPS:

    def __init__(self):
        # Initialize two stacks for the main and minimum values respectively

    def push(self, val):
        # Push the value to the main stack

        if minVal Stack is not empty:
            currentMinimumValue = min(currentValue, minStack[-1])
            append currentMinimumValue to minStack List

        else:
            append currentValue to minStack List


    def pop(self):
        if stack is empty:
            return "Stack is Empty"

        else:
            remove last element from both stacks


    def top(self):
        return last element from stack list

    def getMin(self):
        return the last element from the minValue list

RESULTS:


'''