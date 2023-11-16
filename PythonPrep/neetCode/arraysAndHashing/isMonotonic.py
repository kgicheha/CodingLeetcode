def isMonotonic(array):
    increasing = True
    decreasing = True

    for i in range(len(array) - 1):
        curInt = array[i]
        nextInt = array[i+1]

        if curInt < nextInt:
            # [1,3,4]
            decreasing = False

        elif curInt > nextInt:
            increasing = False

        else:
            continue

    return increasing or decreasing


array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
# True
print(isMonotonic(array))
'''
Link: https://www.algoexpert.io/questions/monotonic-array
'''
'''
GIVEN:
    array of integers
STEPS:

    initialize increasing and decreasing variables and set them both equal to True

    iterate through given array:
        if the current integer < next integer:
            flip the decreasing variable to False:
                this means that the array should be non-increasing

        elif the current integer > next integer:
            flip the increasing variable to False:
                this means that the array should be non-decreasing

        else current integer == next integer:
            continue to the next integer


    return increasig or decreasing


RESULTS:
    return True if array is monotonic
        Array is monotonic if its elements, from left to right,
            are entirely non-increasing, or entirely non-decreasing
'''