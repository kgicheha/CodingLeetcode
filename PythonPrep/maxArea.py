'''
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''
'''
EXAMPLE:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array
[1,8,6,2,5,4,8,3,7]. In this case,
the max area of water (blue section) the container can contain is 49.

'''

'''
GIVEN:
    array of heights
STEPS:


    initialize left pointer = 0
    initilize right pointer  = len(arr) - 1
    initialize cur_height = 0
    initialize cur_length = 0
    initialize max_area = 0

    while left < right:
        calculate the length
            cur_length = right - left + 1

        if arr[right] >= arr[left]:
            cur_height = arr[left]
        else:
            cur_height = arr[right]

        curr_area = cur_length * cur_height

        max_area = max(max_area, cur_area)

        keep the highest value at the two pointers
            if the value at the left pointer <= value at the right poiinter:
                increment left pointer by 1
            else:
                decrement right pointer by 1

    return max_area
RESULT:
    return the max amount of water a container can store
'''

def maxArea(arr):
    left = 0
    right  = len(arr) - 1
    cur_height = 0
    cur_width = 0
    max_area = 0

    while left < right:
        cur_width = right - left

        if arr[right] >= arr[left]:
            cur_height = arr[left]
        else:
            cur_height = arr[right]

        cur_area = cur_height * cur_width

        max_area = max(max_area, cur_area)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    print(max_area)



arr = [1,8,6,2,5,4,8,3,7]
maxArea(arr)