def maxArea(height):
    lp = 0
    rp = len(height) - 1

    res = 0

    while lp < rp:
        curHeight = min(height[lp], height[rp])
        curLength = rp - lp

        curArea = curHeight * curLength

        res = max(res, curArea)

        if height[lp] < height[rp]:
            lp += 1
        else:
            rp -= 1

    return res


height = [1,8,6,2,5,4,8,3,7]
# Output: 49
print(maxArea(height))

'''
Link: https://leetcode.com/problems/container-with-most-water/
'''
'''
GIVEN:
    array of integers height

    formula: area = length * height
STEPS:
    initialize left pointer equal to 0
    initialzie right pointer equal to len(height) - 1

    initialize maxResult equal to 0

    iterate though given array while left < right pointer:
        height = min(height[left pointer], height[right pointer])
        length = difference between left and right pointers

        current height = height * length

        result = max(currentHeight, result)

        if the number at the left pointer is < than the number at the right pointer:
            increment left pointer by 1
                this way you can maximize the height
        else:
            decrement right pointer by 1

    return result

RESULTS:
    Return the maximum amount of water a container can store.

'''
