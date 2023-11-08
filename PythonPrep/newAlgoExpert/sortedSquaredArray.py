def sortedSquaredArray(array):


    # STRATGEY 1: TIME COMPLEXITY: O(nlogn), SPACE COMPLEXITY: O(n)
    # result = []
    # for num in array:
    #     currentSquared = num ** 2
    #     result.append(currentSquared)

    # result.sort()
    # return result


    # STRATEGY 2: Time Comp: O(n), Space Comp: O(n)
    result = []
    lp = 0
    rp = len(array) - 1

    while lp < rp:

        leftSquaredNum = array[lp] ** 2
        rightSquaredNum = array[rp] ** 2

        if leftSquaredNum > rightSquaredNum:
            result.append(leftSquaredNum)
            lp += 1

        else:
            result.append(rightSquaredNum)
            rp -= 1

    return result[::-1]

array = [-10,-1,1,2,3,5,6,8,9]
print(sortedSquaredArray(array))
'''Link: https://www.algoexpert.io/questions/sorted-squared-array'''

'''
GIVEN:
    sorted array
STEPS:

    initialize result array to empty array

    initialize left pointer to 0
    initialize right pointer to the last index

    iterate given array while left pointer is less than right pointer:

        initialize leftSquaredValue equal to value at left pointer multplied by itself
        initialize rightSquaredValue equal to value at right pointer multplied by itself

        if the leftSquaredValue > right SquaredValue:
            append leftSquaredValue
            increment left pointer by 1

        else:
            append rightSquaredValue
            decrement right pointer by 1

    return reversed result

    return reversed result array

RESULT:
    return new array of squared numbers
'''