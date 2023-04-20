'''
Question Link:
https://www.algoexpert.io/questions/four-number-sum
'''

'''
GIVEN:
    array of distinct integers
    targetSum integer
STEPS:
    sort given array

    initialize empty results array
    initialize 3 pointers
        left pointer starts at 1 and end at the 2nd last element
        right pointer starts at last element
        middle pointer starts at 2

    traverse given array:
        while middle pointer < right pointer:
            calc sum of all the values at each pointers

            if currentSum == targetSum:
                push all the items to the results array
            elif currentSum < targetSum:
                increment left pointer by 1
            elif currenSum  > targetSum:
                decrement right pointer by 1


    return results array
RESULT:
    return a 2d array of all the quadruplets in no particular order

'''


# def fourNumberSum(array, targetSum):
#     array.sort()

#     result = []

#     lp = 1
#     md = lp + 1
#     rp = len(array) - 1

#     for value in range(len(array) - 3):
#         while md < rp and lp < len(array) - 2:
#             currentSum = array[value] + array[lp] + array[md] + array[rp]

#             if currentSum == targetSum:
#                 result.append([array[value], array[lp], array[md], array[rp]])
#                 lp += 1
#             elif currentSum < targetSum:
#                 md += 1
#             elif currentSum > targetSum:
#                 rp -= 1

#     return result


def fourNumberSum(array, targetSum):

    sumOfAllPairs = {}
    results =[]

    for i in range(len(array)):

        for j in range(1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum


            if currentSum in sumOfAllPairs:
                sumOfAllPairs[currentSum].extend([array[i], array[j]])
            else:
                sumOfAllPairs[currentSum] = [array[i], array[j]]

    print(sumOfAllPairs)

    for sum, pairs in sumOfAllPairs.items():
        difference = targetSum - sum

        if difference in sumOfAllPairs.keys():
            # print(sumOfAllPairs[difference])
            currentPairs = pairs
            matchedPairs = sumOfAllPairs[difference]
            pairs = currentPairs + matchedPairs
            # print("current pairs: ", currentPairs)
            # print("matched pairs: ", matchedPairs)
            # print("target pairs: ", pairs)
            results.append(pairs)

            # results.append(pairs sumOfAllPairs[difference])


    # return results

# [-1, 1, 2, 4, 6, 7]
array = [7, 6, 4, -1, 1, 2]
targetSum = 16

print(fourNumberSum(array, targetSum))

