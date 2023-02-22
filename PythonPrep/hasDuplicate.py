'''
Given an array and a positive number k,
check whether the array contains any duplicate elements within the range k.
If k is more than the array’s size,
 the solution should check for duplicates in the complete array.
'''
'''
GIVEN:
    array
    positive number k
STEPS:

    initialize empty set to store current item in

    for loop through given array:

        if the current item is in the set:
            print("Duplicate found")

        else:
            add number to set

        if current index is >= to k:
            remove the first elemnt from the set
            that way you are only comparing numbers withing the k window size


    if it goes through entire first for loop without finding duplicates:
        print("No duplicates found")

RESULT:
'''


def hasDuplicate(arr, k):


    window = set()

    for i in range(len(arr)):

        if arr[i] in window:
            print("Duplicates found")

        window.add(arr[i])

        if i >=k:
            window.remove(arr[i-k])

    print("No duplicated found")
arr = [2,2,3,2,1]
k= 2
hasDuplicate(arr, k)