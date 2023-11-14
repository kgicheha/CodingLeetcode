
# STRATEGY 2:
def trap(height):
    if len(height) == 0:
        return 0

    lp = 0
    rp = len(height) - 1

    maxLeft = height[lp]
    maxRight = height[rp]

    res = 0

    while lp < rp:

        if maxLeft < maxRight:
            lp += 1
            maxLeft = max(maxLeft, height[lp])
            rainWater = maxLeft - height[lp]
            res += rainWater
        else:
            rp -= 1
            maxRight = max(maxRight, height[rp])
            rainWater = maxRight - height[rp]
            res += rainWater

    return res
# STRATEGY 1
# def trap(height):

#     maxLeftArray = []
#     maxLeftArray.insert(0, 0)

#     for i in range(len(height) - 1):
#         maxLeft = max(maxLeftArray[i], height[i])
#         maxLeftArray.append(maxLeft)

#     print(maxLeftArray)

#     maxRightArray = []
#     maxRightArray.insert(0, 0)

#     for i in range(len(height)-1, -1, -1):
#         maxRight = max(maxRightArray[0], height[i])
#         maxRightArray.insert(0, maxRight)

#     print(maxRightArray)

#     minValues = []

#     for i in range(len(maxLeftArray)):
#         minVal =  min(maxLeftArray[i], maxRightArray[i])
#         minValues.append(minVal)

#     print("Min Values:",minValues)

#     res = 0

#     for i in range(len(height)):
#         rainWater = minValues[i] - height[i]

#         if rainWater > 0:
#             res += rainWater

#     return res

height = [4,2,0,3,2,5]
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 9
print(trap(height))

'''
Link: https://leetcode.com/problems/trapping-rain-water/
'''
'''
GIVEN:
    N non-negative integers representing an elevation map
    where the width of each bar is 1,
STEPS:

    STRATEGY 1: TIME AND SPACE COMPEXITY: O(n)
        initialize maxLeftArray that keeps track of the maxValue as you iterate given array from left to right
        insert 0 at the beginning of the array
            since that's what our max number will start with

        iterate through given array: from left to right
            update maxNumber if the current number is > than the previous maxNumber
                we want to keep track of the max numbers that we've seen so far

            append the max number at the end of the maxLeftArray


        initialize maxRightArray to empty array
            keeps track of the max Numbers that we've seen so far as we iterate through given array

        iterate though given array: from right to left:
            update maxNumber if the current number is > than the previous maxNumber
                we want to keep track of the max numbers that we've seen so far

            insert the max number at the begginng of the maxRightArray


        initialize minValueArray that Keeps track of the min value between the maxLeftArray and maxRightArray at the same index

        iterate through the maxLeftArray and maxRightArray:
            store the minimum value between the two numbers at the same index
                store to the minValueArray

        initalize result to 0

        iterate through the given array:
            formula = minValue[i] - height[i]

            calculate the number based on this formula

            if the number is > 0:
                add it to the result

        return result


    STRATEGY 2: Time Complexity: O(n), SPACE complexity: O(1)

RESULTS:


'''
