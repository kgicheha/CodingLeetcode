def containsDuplicate(nums):

    # STRATEGY 1: using hashset --> TIME & SPACE COMPLEXITY: O(n)
    # seen = set()

    # for num in nums:
    #     if num in seen:
    #         return True

    #     seen.add(num)

    # return False

    # STRATEGY 2: sorting the given array --> TIME COMPLEXITY: O(n), SPACE COMP: 0(1)

    nums.sort()

    lp = 0
    rp = lp + 1

    while rp < len(nums):
        if nums[lp] == nums[rp]:
            return True
        else:
            lp += 1
            rp += 1

    return False
nums = [1,2,3,1]
print(containsDuplicate(nums))

'''
Link: https://leetcode.com/problems/contains-duplicate/
'''

'''
GIVEN:
    array of integers
STEPS:
    create empty set to store the numbers that have been seen

    iterare through given array:
        if number is in the set:
            return True

        add number to the set

    return False if there are no diplicates

RESULTS:
    return True if any values appears atleast twice in the array
    else,
    return False
'''