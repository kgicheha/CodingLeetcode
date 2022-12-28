'''
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers
where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums,
return this repeated number.

You must solve the problem without modifying the array nums
and uses only constant extra space.
'''

'''
EXAMPLE
Input: nums = [1,3,4,2,2]
Output: 2
'''

'''
GIVEN: linked lists: each value is the index that the current node points to
STEPS:
    create two pointers: fast and slow pointer
        set them equal to 0
    While loop
        set the slow pointer equal to the first element

        if the slow pointer == to the fast pointer
            break out of the loop
        increment fast pointer by 2
        increment slow pointer by 1

    create another slow_pointer and set it equal to 0

    While loop
        keep incrementing the new slow pointer and original slow pointer by 1
        until the two pointers are equal to each other
            once this happens: return the slow pointer


RETURN the beginning of a cycle


TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
'''

def find_duplicate(nums):
    slow_pointer, fast_pointer= 0,0
    while True:
        slow_pointer =nums[slow_pointer]
        fast_pointer =nums[nums[fast_pointer]]
        if slow_pointer == fast_pointer:
            break

    slow_pointer2 = 0
    while True:
        slow_pointer = nums[slow_pointer]
        slow_pointer2 = nums[slow_pointer2]
        if slow_pointer == slow_pointer2:
            print(slow_pointer)


nums = [1,3,4,2,2]
find_duplicate(nums)