'''
Question Link:
algoexpert.io/questions/find-three-largest-numbers
'''
'''
GIVEN:
    array of at least 3 integers
STEPS:

    initialize 3 variables equal to -infinity
        each of the 3 variables will be used to store the 3 highest numbers

    initialize 3 variables to 0
        these will be used to store the index of the 3 highest numbers

    initialize empty result array

    traverse array:
        find the largrst number
        store the numbers and its index in of the variables

    travese array
        find the 2nd largest number
        store the numbers and its index in the variables

    traverse array
        find the 3rd largest number
        store the numbers and its index in the variables

    append the numbers into the result array
RESULTS:
    without sorting,
        return a sorted array of the three largest integers in the input array


Time Complexity --> 0(n) || Space Complexity --> 0(1)
'''

def findThreeLargestNumbers(array):

    maxNum1 = -float("inf")
    index1 = 0

    maxNum2 = -float("inf")
    index2 = 0

    maxNum3 = -float("inf")
    index3 = 0

    result = []

    for i in range(len(array)):
        if array[i] > maxNum1:
            maxNum1 = array[i]
            index1 = i

    for j in range(len(array)):
        if array[j] > maxNum2 and j != index1:
            maxNum2 = array[j]
            index2 = j

    for k in range(len(array)):
        if array[k] > maxNum3 and k != index1 and k != index2:
            maxNum3 = array[k]
            index3 = k

    print(maxNum1, maxNum2, maxNum3)
    result = [maxNum1] + result
    result = [maxNum2] + result
    result = [maxNum3] + result

    return result

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(array))