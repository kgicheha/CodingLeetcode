'''
GIVEN:
    non empty with positive integers of executing times
STEPS:
    sort the given array:
        that helps to work with the smallest numbers 1st
    initialize variable that keeps track of the running sum of the numbers
    initialize variable to keep track of the sum of the previus time + the current value

    traverse the sorted array:
        add the sum of the previous times
        add the value at the current index to the previous times

    return the running sum

RESULTS:
    return the minimum execution time
'''
'''
EXAMPLE 1:
array  = [1, 4, 5]
executed [5, 1, 4]
 0 + 5 + (5 + 1) = 11

EXAMPLE 1 w/ SORTED ARRAY
[1, 4, 5]
0 + (0 + 1) + (0 + 1 + 4) = 6

EXAMPLE 1 possible array
[4, 1, 5]
0 + 4 + (4 + 1) = 9

example 1 possible
[4, 5, 1]
0 + 4 + (4 + 5) = 13
'''

def minRunTime(array):
    array.sort()

    runningSum = 0
    prevTimes = 0

    for time in array:
        runningSum += prevTimes
        prevTimes += time

    return runningSum

array  = [1, 4, 5]
print(minRunTime(array))

'''

'''