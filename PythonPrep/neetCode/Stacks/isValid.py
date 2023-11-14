def isValid(s):
    lookup = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack =[]

    for char in s:
        if char in lookup.values():
            stack.append(char)

        elif (stack) and (stack[-1] == lookup[char]):
                stack.pop()

        else:
                return False

    return stack == []

s = "()[]{}"
# Output: true
print(isValid(s))
'''
Link: https://leetcode.com/problems/valid-parentheses/
'''
'''
GIVEN:
    a string s containing just the characters
    '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
STEPS:
    store the open parathensis in a hashMap, with the close parathesis as its value

    initialize empty stack array

    iterate through each character c of the string s:
        if character's closing parathesis is in hashMap values:
            add character to the stack

        elif stack is not empty and the last element in the stack is equal to the value of the character in the lookup table:
            remove the element from the stack

        else:
            return false because it means that there are unmatched opening parentheses


    return True if the stack is empty



RESULTS:
    return True if input string is valid:
        An input string is valid if:
            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.
            Every close bracket has a corresponding open bracket of the same type.


'''
