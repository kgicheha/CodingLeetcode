def twoSum(nums, target):

    numDict = {}

    for i in range(len(nums)):
        difference = target - nums[i]

        if difference in numDict:
            return [numDict[difference], i]

        numDict[nums[i]] = i

    return False

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
'''
Link: https://leetcode.com/problems/two-sum/
'''

'''
GIVEN:
    An array of integers nums containing n elements,
    an integer target.
STEPS:
    # STRATEGY 1: TIME and SPACE COMPL: O(n)
        create empty dictionary

        iterate through given array:
            difference = target - num

            if the number in the dictionary:
                return [its index, index of the number that matches it

            else:
                store the index and and number in the dictionary

RESULTS:


'''

