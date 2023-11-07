'''
Link: https://www.algoexpert.io/questions/two-number-sum

'''

'''
GIVEN:
   1. non-empty array
   2. target sum

STEPS:

    STRATEGY 1: TIME & SPACE Complexity: O(n)
        1. create empty dictionary
        2. traverse given array
            subtract the current number from the target sum

            if the result is in the dictionary,
                return [the number that matches it, current number]

            else:
                store the result in the dictionary

        if you traverse the entire array and no matches are found:
            return an empty array
RESULT:
    return array


'''


def twoNumberSum(array, targetSum):
    difference = {}

    for num in array:
        cur_difference = targetSum - num

        if cur_difference in difference:
            return [num, cur_difference]

        else:
            difference[num] = cur_difference

    return []

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(twoNumberSum(array, targetSum))