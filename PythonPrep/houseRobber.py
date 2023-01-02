'''
198. House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them
is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses
 were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without
alerting the police.
'''

'''
EXAMPLE 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1)
and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
'''

'''
GIVEN: array of numbers representing the amount of money of each huose
STEPS:
    DYNAMIC PROGRAMMING
    edge cases:
        if nums is 0 return 0

    iterate given array starting from the 1st value to the end of the array
        if the length of nums is equal to 1
            current value will equal the max value between
                1. itself
                2. the adjacent house value
        else:
            current value will be the max value between
                1. the value of the adjacent House
                2. sum of the current value and the value of the house thats 2 indeces before itself
    return the value of the last index
RETURN: maximum amount of money you can rob without alerting the police


TIME Comp: O(n)
Space Comp: O(1)
'''

def rob(nums):

    for i in range(1, len(nums)):
        if i == 1:
            nums[i] = max(nums[i], nums[i-1])
        else:
            prev_house_max = nums[i-1]
            cur_house_max = nums[i]+nums[i-2]
            nums[i] = max(cur_house_max, prev_house_max)

    return nums[-1]

