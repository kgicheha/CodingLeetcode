'''
11. Container With Most Water
You are given an integer array height of length n.
There are n vertical lines drawn such that the
two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

'''
EXAMPLE
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by
array [1,8,6,2,5,4,8,3,7]. In this case,
the max area of water (blue section) the container can contain is 49.

'''

'''
GIVEN: array of heights
STEPS:
     define two pointers: left and right
        set the left pointer to be the first element in the array
        set the right pointer to be the last element
    define area and set it equal to 0

    While the two pointer dont intersect
        Calculate minimum height
            the minimum value between the left and right pointer
        Find the width
            width = the distance between the two pointers
            difference between the right and left pointer
        Find the current area
            area = height * width

        if new area is greater than the current max area,
            set the new area to be the new max area

        Increment or decrement the pointer that has the smaller height
            keep the highest height between the two pointers

    RETURN the max area

'''

def max_area(height):
    left_pointer = 0
    right_pointer  = len(height) - 1
    max_water = 0

    while(left_pointer < right_pointer):
        current_height = min(height[left_pointer], height[right_pointer])
        current_width = right_pointer - left_pointer

        current_water = current_height * current_width

        max_water = max(max_water, current_water)

        if(height[left_pointer] < height[right_pointer]):
            left_pointer +=1
        else:
            right_pointer -= 1

    print(max_water)


height = [1,8,6,2,5,4,8,3,7]
max_area(height)
