def threeSum(nums):
    nums.sort()

    res = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        lp =  i+1
        rp = len(nums) - 1

        while lp < rp:
            curSum = nums[i] + nums[lp] + nums[rp]

            if curSum > 0:
                rp -= 1
            elif curSum < 0:
                lp += 1
            else:
                res.append([nums[i], nums[lp], nums[rp]])

                while lp < rp and nums[lp] == nums[lp + 1]:
                    lp += 1

                while lp < rp and nums[rp] == nums[rp - 1]:
                    rp -= 1

                lp += 1
                rp -= 1

    return res

nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
print(threeSum(nums))
'''
Link: https://leetcode.com/problems/3sum/
'''

'''
GIVEN:
    integer of nums
STEPS:
    sort the given array

    initialize empty array to store results

    iterate through given array length - 2:

        if i > 0 and the current number is equal to the previous number:
            continue

        initialize left pointer to 1
        initialize right pointer to last index

        while left pointer < right pointer:

            if current number is not equal to the number at the left and right pointer:

                calculate sum at the current position + number at left pointer + number at right pointer

                if the sum is > 0:
                    decrement right pointer by 1

                elif sum is < 0 :
                    increment left pointer by 1

                else:
                    append [nums[i], nums[lp], nums[rp]]

                    while left pointer is < rp and number at left pointer is equal to the number thats to the right of it
                        increment left pointer by 1
                            since we want unique values

                    while left pointer is < right pointer and number at right pointer is equal to the number thats to the left of it
                        decrement right pointer by 1
                            since we want unique values

                    increment left pointer by 1
                    decrement right pointer by 1

    return result

RESULTS:

'''