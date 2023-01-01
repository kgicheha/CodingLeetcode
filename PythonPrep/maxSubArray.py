'''
53. Maximum Subarray
Given an integer array nums, find the subarray
with the largest sum, and return its sum
'''

'''
EXAMPLE 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

EXAMPLE 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
'''

'''
GIVEN: array of numbers,
STEPS:
    create a variable that stores the max sum and intialize it to the first value in the number array
    create a current Sum variable and initialize it to 0

    iterate given array of number
        add the current number to the current sum
        if the current number is greater than the current sum
            set the current sum equal to the current number
            this will get rid of the current numbers that were included in the sum
            and start the count to begin at the current number

        if the current sum is greater than the max sum
            set the current sum as the new max sum

RESULT: the sum of the largest

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
'''

def maxSubArray(nums):
    max_sum = nums[0]
    cur_sum = 0

    for n in nums:
        cur_sum += n
        cur_sum = max(cur_sum, n)
        max_sum = max(max_sum, cur_sum)
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
