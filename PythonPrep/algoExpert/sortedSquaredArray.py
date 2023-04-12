'''
Question Link:
https://www.algoexpert.io/questions/sorted-squared-array
'''
'''
GIVEN:
    non-empty array of SORTED integers
STEPS:
    create empty array to store result
    traverse through given array
       multiply number by itself
        push answer to result
    return result array
RESULT:
    return a new array of the same length with the squares of the original integers
        also in sorted order
'''
def sortedSquaredArray(array):

    # SOLUTION 1: NON-DESTRUCTIVE USING EXTRA SPACE
        # 0(n) time complexity | O(n) space complexity
    result = []

    for value in array:
        squared = value * value
        result.append(squared)

    result.sort()
    return result

    #

array = [1,2,3,5,6,8,9]
print(sortedSquaredArray(array))
