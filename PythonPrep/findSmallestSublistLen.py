'''
Given an array of positive integers, find the smallest subarray’s
length whose sum of elements is greater than a given number k.


Example:

Input:  {1, 2, 3, 4, 5, 6, 7, 8}, k = 20
Output: The smallest subarray length is 3
Explanation: The smallest subarray with sum > 20 is {6, 7, 8}

'''
'''
GIVEN:
    array of integers
    k number
STEPS:
    initiliaze left and right pointers to 0
    initialize min length that've seen so far
    initialize windowSum to 0
    smallest_sub_arry =[]

    loop through given array:
        add current element to the window sum

        while (window sum > target) and (left pointer <= right pointer):

            inilitialize current window size equal to (right pointer - left pointer + 1)


            if min_length == 0:
                set min length = current window size
                smallest_sub_arry = arr from left to right pointer
            elif min_length > current window size:
                min_length = current window size
                smallest_sub_arry = arr from left to right pointer

            reduce the size of the window by:
                removing the value in the left pointer from the window sum
                incrementing left pointer by 1

    return min_length

RESULT:
    smallest subarray length whose sum of elements is > than k
'''



def findSmallestSublistLen(arr, k):

    left, right = 0, 0
    min_length, window_sum  = 0,0
    smallest_sub_arry = []


    for right in range(len(arr)):

        window_sum += arr[right]


        while (window_sum > k) and (left <= right):
            cur_window_size = right - left + 1

            if min_length == 0:
                min_length = cur_window_size
                smallest_sub_arry = arr[left:right+1]
            elif min_length > cur_window_size:
                min_length = cur_window_size
                smallest_sub_arry = arr[left:right+1]


            window_sum -= arr[left]

            left += 1

    print(min_length)

    print(smallest_sub_arry)

arr = [10, 21, 3, 4, 5, 6, 7, 8]
k = 20
findSmallestSublistLen(arr, k)