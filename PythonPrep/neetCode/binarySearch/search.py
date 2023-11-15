def search(nums, target):

    lp = 0
    rp = len(nums) - 1

    while lp < rp:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            lp = mid + 1

        else:
            rp = mid - 1

    return -1

Input: nums = [-1,0,3,5,9,12]
target = 9
# Output: 4
print(search(nums, target))

'''
Link: https://leetcode.com/problems/binary-search/
'''

'''
GIVEN:
    array of sorted numbers
    target number

STEPS:

    initialize left and right pointer equals to 0 and len(nums)-1, respectively

    while left < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:

            left = mid + 1
        else:
            right = mid - 1
    return -1
RESULTS:
    if the target exists:
        return its index
    else:
        return -1
'''