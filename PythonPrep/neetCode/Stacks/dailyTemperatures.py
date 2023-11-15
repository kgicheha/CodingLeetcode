def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []

    for idx, temp in enumerate(temperatures):

        while stack and temp > stack[-1][0]:

            stackTemp, stackIdx = stack.pop()


            difference = idx - stackIdx

            res[stackIdx] = difference

        stack.append([temp, idx])

    return res
temperatures = [73,74,75,71,69,72,76,73]
# temperatures = [30,40,50,60]
# Output: [1,1,4,2,1,1,0,0]
print(dailyTemperatures(temperatures))
'''
Link: https://leetcode.com/problems/daily-temperatures/
'''

'''
GIVEN:
    an array of integers representing daily temperature
STEPS:

    SOLUTION:

    Initialize result array list to the len of of input array
    intialize stack to empty array list

    iterate though given array:
        while stack is not empty AND the current temperate is > than the temperature in the last element in the stack:
            pop the last element out of the stack
            calculate the difference between the current index and the index from the popped element
            append this value into the result array at the corresponding index


        append the temp and index to the stack

    return the result


RESULTS:
    return an array answer such that answer[i] is the number of
    days you have to wait after the ith day to get a warmer temperature

     If there is no future day for which this is possible,
        keep answer[i] == 0 instead.
'''