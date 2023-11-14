def generateParenthesis(n):
    # only add open paranthesis if closed < open
    # only add a closing paranthesis if closed < open
    # valid if open == closed == n

    stack = []
    res = []

    def backtrack(openCount, closedCount):

        if openCount == closedCount == n:
            joinedResult = "".join(stack)
            res.append(joinedResult)
            return

        if openCount < n:
            stack.append("(")
            backtrack(openCount + 1, closedCount)
            stack.pop()

        if closedCount < openCount:
            stack.append(")")
            backtrack(openCount, closedCount + 1)
            stack.pop()

    backtrack(0, 0)
    return res


n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
print(generateParenthesis(n))

'''
Link: https://leetcode.com/problems/generate-parentheses/
'''
'''
GIVEN:
    Given n pairs of parentheses
STEPS:

    intialize stack equal to empty array
    initialize results equal to empty array

    create recursice function that will add the different combinations:
        pass in the a count that keeps track of the count of open parenthesis in the stack
            and a count that keeps track of the count of the closed parenthesis in the stack


        BASE CASE: if openCount == closedCount == n pairs of paranethesis:
            join the items in the stack
            append the items to the results
            return

        if the openCount < n:
            append the open paranthesis "(" to the stack
            call the recursive function with a increment of 1 to the openCount

            pop the last element in the stack:
                this will help to create another combination of paranthesis

        if the closedCount < openCount:
            append the closed paranthesis ")" to the stack
            call the recursive function with a increment of 1 to the closedCount



    call the recursive function with 0 and 0 as its initial arguments for the open and closed Counts
    return the result
RESULTS:
    write a function to generate all combinations of well-formed parentheses.



'''