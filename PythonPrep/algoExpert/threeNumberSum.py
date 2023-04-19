'''
Question Link:
https://www.algoexpert.io/questions/three-number-sum
'''

'''
GIVEN:
    array of values
    targetSum
STEPS:
    sort the given array
    initialize results array

    initialize 3 pointers
        pointer 1: starts from 0
        pointer 2: starts at pointer1 + 1 and increments
        pointer 3: starts at last element and decrements





    traverse given array while pointer1 and pointer3 have not crossed each others paths
        initialize currrent Sum variable and set it equal to the sum of the 3 numbers at on the pointers

        if current sum < target sum:


        else if current sum > target sum:

        else
            add the numbers to the results array as an array

    return empty array if no triplet is found

RESULT:
    return the triplets that add up to the targetSum
    else:
        return an empty array if there are no matches found


'''
def threeNumberSum(array, targetSum):
    array.sort()

    result = []

    for value in range(len(array) - 2):
        lp =  value + 1
        rp = len(array) - 1

        while lp < rp:

            currentSum = array[value] + array[lp] + array[rp]
            print(currentSum)

            if currentSum < targetSum:
                lp += 1
            elif currentSum > targetSum:
                rp -= 1
            elif currentSum == targetSum:
                result.append([array[value], array[lp], array[rp]])
                lp += 1
                rp -= 1

    return result



# [-8, -6, 1, 2, 3, 5, 6, 12] --> sorted
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

print(threeNumberSum(array, targetSum))

