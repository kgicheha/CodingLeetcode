'''
1. Two Sum
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

'''
'''
EXAMPLE 1
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


EXAMPLE 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
'''

'''
GIVEN: array of numbers, target number
STEPS:
    create an hashMap
       will store the current number and its index

    loop through array
        get the difference between the current number and the target value

        if the difference is in the hashMap
            return [index of the difference, current index]
        else:
            store the current number to the HashMap with its index as its value
RETURN array of the indeces that sum up to given target number
'''


def twSum(nums, target):
    prevMap = {} # value: index

    for i, n in enumerate(nums):
        diff = target - n

        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return


nums = [3,2,4]
target = 6
print(twSum(nums, target))
