'''
1413. Minimum Value to Get Positive Step by Step Sum

Given an array of integers nums,
you start with an initial positive value startValue.

In each iteration, you calculate the
step by step sum of startValue plus
elements in nums (from left to right).

Return the minimum positive value of startValue
such that the step by step sum is never less than 1.
'''

'''
Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4,
in the third iteration your step by step sum is less than 1.
step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2
'''
'''
GIVEN:
    array of integers
STEPS:
    create sum variable and initialize it to 0
    create result variable and initialize it to 0

    loop through given array
        the goal is to find the minimum sum value
            then store it to the result variable

    find the value that you would need to add to the minimum sum to get to 1
        return 1 + the absolute value of the result
RESULT:
    minimum positive value
'''

def minStartValue(nums):
    sum = 0
    res = 0

    for n in nums:
        sum += n
        res = min(res, sum)

    return 1 + abs(res)



nums = [1,-2,-3]
print(minStartValue(nums))