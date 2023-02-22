'''
Given an array and an integer k,
find the count of distinct elements in every subarray of size k.

'''
'''
GIVEN:
    array of integers
    k postive number
STEPS:
    intialize empty set
    intialize count that keeps track of distinct element in window

    for loop through given array:

        if current element is not in set:
            incremement count by 1

        else:
            add current element to set

        if i >= k
            remove the first element in the set

RESULT:
'''

def findDistinctCount(arr, k):

    left = 0
    right = k

    while right <= len(arr):
        distint_len = len(set(arr[left:right]))

        cur_window = arr[left:right]

        print(f"The count of distinct elements in subarray", cur_window, "is", distint_len)

        left += 1
        right += 1


arr =[2, 1, 2, 3, 2, 1, 4, 5]
k = 5

findDistinctCount(arr, k)