'''
Question link:
https://www.algoexpert.io/questions/two-number-sum
'''

'''
GIVEN:
    1. non-empty array of distinct integers
    2. target sum
STEPS:
    sort the given array
    create two pointers: left and right
        initialize left pointer to 0
        initialize right pointer to the last number in the array

    while the left pointer and right pointer dont overlap:
        add the two numbers in the two pointers

        if the sum of numbers is LESS THAN targetSum:
            increment the left pointer by 1
        else if the sum fo the numbers is MORE THAN targetSum:
            decrement the right pointer by 1
        else if the sum of the numbers is EQUAL to the targetSum:
            return the values in an array

    if a pair is not found in the given array:
        return an empty array
RESULT:
    array of the pairs that add up to the targetSum
'''

def twoNumberSum(array, targetSum):

    # SOLUTION 1: USING AN HASH TABLE
        # Time Complexity: O(n)
        # Space Complexity: O(n)
    # seen = {}
    # result = []

    # for value in array:
    #     dif = targetSum - value

    #     if dif not in seen:
    #         seen[value] = dif
    #     else:
    #         result = [seen[dif], dif]
    #         return result
    # return result


    # SOLUTION 2: USING SORT AND TWO POINTERS
    result = []
    array.sort()

    lp = 0
    rp = len(array) - 1

    while lp < rp:
        currSum = array[lp] + array[rp]

        if currSum < targetSum:
            lp += 1
        elif currSum > targetSum:
            rp -= 1
        elif currSum == targetSum:
            result = [array[lp], array[rp]]
            return result

    return result

array = [3,5,-4,8,11,1,-1,6]
targetSum = 10

print(twoNumberSum(array, targetSum))