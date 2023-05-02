'''
Question Link:
https://www.algoexpert.io/questions/binary-search
'''

'''
GIVEN:
    1. sorted array of integers
    2. target integer
STEPS:
    initialize left pointer to 0
    initialize right pointer to the last value in the array

    while left pointer is <= right pointer:

        initialize a mid pointer index:
            length of array // 2

        if middle value is equal to the target value:
            return its index

        elif target value < middle value:
            set right pointer to equal middle index - 1
        elif target value > middle value:
            set the left pointer equal to middle index + 1


    if you go traverse array and the value is not found:
        return -1
RESULTS:
    if the target integer is contained in the given array:
        return its index:
    else:
        return -1


TIME COMPLEXITY: O(log N) || Space Complexity: O(1)
'''

def binarySearch(array, target):
    lp = 0
    rp = len(array) - 1

    while lp <= rp:

        middleIndex = (lp + rp) // 2

        if array[middleIndex] == target:
            return middleIndex

        elif target < array[middleIndex] :
            rp = middleIndex - 1

        elif target > array[middleIndex]:
            lp = middleIndex + 1

    return -1


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
print(binarySearch(array, target))
