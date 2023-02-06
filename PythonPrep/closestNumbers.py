'''
Given a list of unsorted integers, ,
find the pair of elements that have the smallest absolute difference between them.
If there are multiple pairs, find them all.
'''

'''
GIVEN:
    array of unsorted numbers
STEPS:

    edge case: empty array --> return arr
    edge case: if arry has 1 item --> return item


    sort the given array
    create a 2 pointers variable
        1. left pointer: starts at arr[0]
        2. right pointer: start at arr[0] + 1
    create an empty array that will store the pairs
    create a variable that store the minimum absolute value
        initialize to be the absolute difference the first and second element

    loop through given array
        get the differnece between the current element and the current element + 1

        if the difference is lower than the current lowest difference:
            set this as the new current lowest difference
            reset the result array back to empty
            add this pair to the array

        if the difference is equal to the current lowest difference:
            add the pair to the array

        increment left pointer by 1
        set right pointer to be left pointer + 1


RETURN:
    return an array of the pair of numbers, that has the smallest absolute difference betweent them
'''

def closestNumbers(arr):
    arr.sort()
    print(arr)

arr = [5,2,3,4,1]
closestNumbers(arr)