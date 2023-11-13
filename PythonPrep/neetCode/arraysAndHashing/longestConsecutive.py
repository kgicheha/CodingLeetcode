def longestConsecutive(nums):

    # STRATEGY 1: sorting --> TIME COMPLEXITY O(nlogn), SPACE = O(n)
    nums.sort()

    consecutiveCount = 0

    lp = 0
    rp = lp + 1

    while rp <= len(nums) - 1:
        if abs(nums[rp] - nums[lp] == 1) or (nums[rp] == nums[lp]):
            consecutiveCount += 1
        else:
            consecutiveCount = 0

        rp += 1
        lp += 1


    return consecutiveCount


nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))
'''
Link: https://leetcode.com/problems/longest-consecutive-sequence/
'''

'''
GIVEN:
    an unsorted of array of integers
STEPS:
RESULT:
    return the length of the longest consecutive elements sequence

'''