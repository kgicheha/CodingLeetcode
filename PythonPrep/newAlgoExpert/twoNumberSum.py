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


    STRATEGY 2: 2 pointer solution --> TIME COMPLEXITY: O (nlogn), SPACE COMPLEXITY: O(1)

        sort given array

        intialize left pointer to 0
        initialize right pointer to last index of the given array


        iterate through given array

            add the number at the left pointer and the number at the right pointer

            if the sum of both are > given target:
                move the right pointer to the left by 1

            else if the sum of both are < given target:
                move the left pointer to the right by 1

            else:
                return [left pointer's value, right pointer's value]


        return []


RESULT:
    return array


'''


def twoNumberSum(array, targetSum):
    # STRATEGY 1:
    # difference = {}

    # for num in array:
    #     cur_difference = targetSum - num

    #     if cur_difference in difference:
    #         return [num, cur_difference]

    #     else:
    #         difference[num] = cur_difference

    # return []


    # STRATEGY 2:
    array.sort()

    lp = 0
    rp = len(array) - 1


    while lp < rp:
        current_sum = array[lp] + array[rp]

        if current_sum > targetSum:
            rp -=1
        elif current_sum < targetSum:
            lp += 1
        else:
            return [array[lp], array[rp]]

    return []

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(twoNumberSum(array, targetSum))