def twoSum(numbers, target):
    lp = 0
    rp = len(numbers) - 1

    while lp < rp:
        curSum = numbers[rp] + numbers[lp]

        if curSum > target:
            rp -= 1
        elif curSum < target:
            lp += 1
        else:
            return [lp + 1, rp + 1]

numbers = [2,3,4]
target = 6
# Output: [1,2]
print(twoSum(numbers, target))

'''
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

'''

'''
GIVEN:
    array of sorted non-decreasing numbers
STEPS:
    initialize left pointer to 0
    initialize right pointer to last element

    iterate through given array while lp pointer is < right pointer:
        calculate sum between the number at the right pointer and the number at the left pointer

        if the difference is > target:
            decrement right pointer by 1

        elif the difference is< target:
            increment left pointer by 1

        else:
            return [lp, rp]
RESULTS:

'''
