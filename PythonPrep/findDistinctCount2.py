'''
Given an array of sorted integers that may contain several duplicate elements,
count the total number of distinct absolute values in it.
'''
'''
Example:
Input:  { -1, -1, 0, 1, 1, 1 }
Output: The total number of distinct absolute values is 2 (0 and 1)
'''

'''
GIVEN:
    array
STEPS:
    initialize empty set
    initialize count

    loop through given array
RESULT:
    total number of distict absolute values
'''
def findDistinctCount(arr):
    seen = set()
    count = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = -arr[i]

        if arr[i] not in seen:
            count += 1
            print(arr[i])

        seen.add(arr[i])

    print(count)

arr = [-1, -1, 0, 1, 1, 1 ]
findDistinctCount(arr)