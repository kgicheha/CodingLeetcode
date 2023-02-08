
'''
Given an array a of n integers and a number, ,
perform d left rotations on the array. Return the updated
array to be printed as a single line of space-separated integers.

'''

'''
GIVEN:
    1. array of integers
    2. number of units to shift to the left
STEPS:
    create empty arry
    splice given array from the given unit to the end
    splice from beginning to the given array

RESULT:
    return the updated arry with the shifted units
'''

def rotLeft(a, d):
    slice1 = a[d::]
    slice2 = a[0:d]
    print(slice1 + slice2)


a =[1,2,3,4,5]
d=4
rotLeft(a, d)
