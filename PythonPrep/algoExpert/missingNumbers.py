'''
Question Link:
https://www.algoexpert.io/questions/missingNumbers
'''

'''
GIVEN:
    unordered list of unique integers in the range [1,n]
        n --> repesents the length of nums + 2

STEPS:

    BRUTE FORCE --> Time Complexity: 0(n) || Space Complexity: O(n)

        initialize empty results array

        create a set of the given array --> so that you can only work with the non-repeating values

        start from 1 to len(given array) + 3 --> want to to + 3 inorder to include the last element
            check to see whether number is in given array

            if number is NOT in given array:
                add it to the result array

        return results array



RESULTS:
    return a new SORTED list with the missing numbers

'''


def missingNumbers(nums):

    result = []

    includedValues = set(nums)

    for value in range(1, len(nums) + 3):

        if value not in includedValues:
            result.append(value)

    return result

nums = [1,4,3]
print(missingNumbers(nums))