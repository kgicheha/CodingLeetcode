'''
Given an array of size N.
Find the largest sum of the contiguous subarray within the array
'''

'''
GIVEN:
    array
STEPS:
    KADANE'S ALGORITHM

    initialize:
        max_so_far = arr[0]
        global_max = 0


    loop for each element in the array
        global_max = global_max + arr[i]

        if global_max < 0:
            global_max = 0

        elif (max_so_far < global_max):
            max_so_far = max_ending

    return global_max
RESULT:
    return the largest sum of the contigious subarray
'''

def largestsumSubarray(arr):

    current_sum = 0
    max_so_far = arr[0]

    for i in range(len(arr)):
        current_sum = current_sum + arr[i]

        if current_sum < 0:
            current_sum = 0

        # elif (max_so_far < current_sum):
        #     max_so_far = current_sum

        max_so_far = max(max_so_far, current_sum)

    print(max_so_far)

largestsumSubarray([-2,-3,4,-1,-2,1,5,-3])