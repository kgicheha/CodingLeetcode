def longestConsecutive(nums):

    numsSet = set(nums)
    max_length = 0

    for i in range(len(nums)):
        if nums[i] - 1 not in numsSet:
            current_length = 0

            while (nums[i] + current_length) in numsSet:
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))
'''
Link: https://leetcode.com/problems/longest-consecutive-sequence/
'''

'''
GIVEN:
    an unsorted of array of integers
STEPS:
    STRATEGY 1: using hashSet --> TIME and SPACE COMP O(n)
    intialize set of the given nums array
    initialize max_length to 0

    iterate through given nums array
        if the (current number - 1) is not in set: --> meaning this the beginning of a consective numbers
            initialize current length equal to 0

            while current number + current length in set:
                increment length by 1

            update the max_length if the current length is higher than it


    return max_length
RESULT:
    return the length of the longest consecutive elements sequence

'''