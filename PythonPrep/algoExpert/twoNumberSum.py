'''
Question link:
https://www.algoexpert.io/questions/two-number-sum
'''

'''
GIVEN:
    1. non-empty array of distinct integers
    2. target sum
STEPS:
RESULT:
'''

def twoNumberSum(array, targetSum):
    # SOLUTION 1: USING AN OBJECT
        # Time Complexity: O(n)
        # Space Complexity: O(n)
    seen = {}

    for value in array:
        dif = targetSum - value

        if dif not in seen:
            seen[value] = dif
        else:
            result = [seen[dif], dif]
            return result
    return []


    # SOLUTION 2:

array = [3,5,-4,8,11,1,-1,6]
targetSum = 10

print(twoNumberSum(array, targetSum))