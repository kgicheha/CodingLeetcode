'''
Given an integer array, find a subarray having a given sum in it.
'''
'''
Example:
Input:  nums[] = {2, 6, 0, 9, 7, 3, 1, 4, 1, 10}, target = 15
Output: {6, 0, 9}
'''
'''
GIVEN:
    arry and a target
STEPS:
    initilize left and right pointers to 0
    initilize current sum to 0

    loop through given array:

        while right < len(array):
            add current element to sum

            if current sum == target:
                print(arr[left:rigt])
            elif current sum < target:
                increment right by 1
                    this will increase the window size by 1

RESULT:

'''

def findSublist(arr, target):

    left, right = 0, 0

    window_sum = 0

    for left in range(len(arr)):
        right = left
        while (right < len(arr)) and (window_sum < target) :
                window_sum += arr[right]
                right += 1

        if window_sum == target:
            print("Sublist found",arr[left:right])
            # return

        window_sum = 0

arr = [2, 6, 0, 9, 7, 3, 1, 4, 1, 10]
target = 15
findSublist(arr, target)