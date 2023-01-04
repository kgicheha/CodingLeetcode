'''
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2,
sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged,
 and the last n elements are set to 0 and should be ignored.
 nums2 has a length of n.

'''

'''
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6]
with the underlined elements coming from nums1.

'''

'''
GIVEN:
    two integer arays that are NOT SORTED
    two integers that represent the number of elements in nums1 and num2, respectively
STEPS:
    create pointer to point to the m + n -1 in nums1 array aft
        meaning where the last value will be when both arrays are merged

    loop array while the lengths of both arrays are more than 0

        if the current value in nums1 is greater than the current value in num2 array
            set the value of the pointer to equal nums1 value
            decrement m by 1
            decrement pointer by 1
        else
            set the value of the pointer equal to nums2 value
            decrement n by 1
            decrement pointer by 1

        edge case: when the pointer reaches the first element of the nums1 array, however there are still values left in the nums 2 array:
            set the value of the pointer equal to the last value in the nums2 array
            decrement n by 1
            decrement pointer by 1

RETURN: dont return anything, merge nums1 as a sorted array


TIME Complex: O(n)
SPACE Complex: O(1)
'''


def merge(nums1, m, nums2, n):
    last = (m + n) - 1
   # merge in reverse order
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1

        last -= 1

    # fill nums1 with left over elements in nums2
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1
