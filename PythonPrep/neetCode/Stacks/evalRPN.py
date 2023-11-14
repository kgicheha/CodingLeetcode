def evalRPN(tokens):
    stack = []

    for char in tokens:
        if char == "+":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 + num2)

        elif char == "-":
            num1 = stack.pop()
            num2 = stack.pop()

            stack.append(num2 - num1)

        elif char == "*":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 * num2)

        elif  char == "/":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(int(num2 / num1))

        else:
            stack.append(int(char))

    return stack[0]

# tokens = ["2","1","+","3","*"]
tokens = ["3","11","5","+","-"]
# Output: 9
print(evalRPN(tokens))

'''
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''
'''
GIVEN:
    array of numbers and operations
STEPS:
    initialize stack equal to empty list

    iterate through given array list:
        if char == "+":
            pop the last 2 elements from the stack
            add them together
            append the result back to the stack

        elif char == "-":
            pop the last 2 elements from the stack
            subtract second element from first one
            append the result back to the stack

        elif char == "*":
            pop the last 2 elements from the stack
            multiply them together
            append the result back to the stack

        elif char == "/":
            pop the last 2 elements from the stack
            divide second element from first one
            append the result back to the stack

        else: --> character is a number
            change the character to an integer
            append the integer to stack

    return the last element in stack
RESULTS:
    Return an integer that represents the value of the expression.
'''