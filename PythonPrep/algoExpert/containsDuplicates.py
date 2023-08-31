'''
Link: https://leetcode.com/problems/contains-duplicate/

'''
'''
GIVEN:
    array of numbers
STEPS:
    SOLUTION 1: TIME AND SPACE COMPLEXITY: O(n)
        1. create empty set that keeps track of each number
        2. iterate through given array:
            if number is not in set, add it
            else if number is in set, return True

        return False if it goes through the given array successfully

RESULT:
    return True, if any values appears AT LEAST TWICE in the array
    else return False if every element is DISTINCT


'''
def containsDuplicates(nums):
    seen = set()

    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            return True

    return False

nums = [1,2,3,4]
print(containsDuplicates(nums))


