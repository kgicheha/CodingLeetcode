'''
167. Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers
that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2,
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution.
You may not use the same element twice.
'''

'''
EXAMPLE 1
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9.
Therefore, index1 = 1, index2 = 2. We return [1, 2].
'''
'''
GIVEN: array of numbers and target number
STEPS:
    TWO POINTER APPROACH since array is sorted
    set the left pointer equal to 0
    set the right pointer equal to the last index

    while left pointer is less than the right pointer:
        sum the the two pointer

        if current sum is greater than the target
            decrease the sum by taking the right pointer and shifting it to the left
        elif current sum is less than the target
            increase the sum by taking the right pointer and shifting it to the right
        else:
            return [left pointer + 1, right pointer + 1]
RETURN: array of the two indeces that sum up to given target number


TIME COMP: O(n)
SPACE COMP: O(1)
'''

def twoSum(numbers, target):

    lp = 0
    rp = len(numbers) - 1

    while lp < rp:
        cur_sum = numbers[lp] + numbers[rp]

        if cur_sum > target:
            rp -= 1
        elif cur_sum < target:
            lp += 1
        else:
            return [lp + 1, rp + 1]

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))