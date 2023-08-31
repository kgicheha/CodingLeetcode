'''
Link: https://leetcode.com/problems/contains-duplicate/

'''
'''
GIVEN:
    array of numbers
STEPS:
    1. create empty set that keeps track of each number
    2. iterate through given array:
        if number is not in set, add it
        else if number is in set, return False

    return False if it goes through the given array successfully

RESULT:
    return True, if any values appears AT LEAST TWICE in the array
    else return False if every element is DISTINCT

TIME AND SPACE COMPLEXITY: O(n)
'''
def containsDuplicates(nums):
    return True

