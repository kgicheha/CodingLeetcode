def threeNumSum(array, targetSum):

    result = []

    array.sort()

    for i in range(len(array) - 2):

        lp = i + 1
        rp = len(array) - 1


        while lp < rp:

            cur_sum = array[i] + array[lp] + array[rp]

            print(cur_sum)

            if cur_sum > targetSum:
                rp -= 1

            elif cur_sum < targetSum:
                lp += 1
            else:
                result.append([array[i], array[lp], array[rp]])
                lp += 1
                rp -= 1

    return result

array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
print(threeNumSum(array, targetSum))


'''Link: https://www.algoexpert.io/questions/three-number-sum '''

'''
GIVEN:
    1. An non-empty array of integers
    2. target sum.

STEPS:
    sort the given array

    initilize empty result array

    iterate through sorted array: --> have to stop at the third last element in order to account for the left and right pointers

        initialize left pointer to 1
        initialize right pointer to len(array) - 1

        add current number + number at left pointer + number at right pointer

        while left pointer < right pointer:

            if current sum > targetSum:
                reduce the sum by decrementing the right pointer by 1

            else if current sum < targetSum:
                increase the sum by incrementing the left pointer by 1

            else:
                append the triplet in the result array
                AND move both pointers towards each other
                    if you only move the right pointer, the current sum will be less than the targetSum
                    if you only move the left pointer, the curren sum will be more than the target Sum

    return the result







        if the sum is >
RESULT:
'''



