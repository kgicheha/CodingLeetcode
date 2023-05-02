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
    initialize right pointer to length of the array

    while left pointer is < right pointer:

        initialize a mid pointer index:
            length of array // 2


        if middle value is equal to the target value:
            return its index

        elif middle value is < target value:
            set right pointer to equal middle index - 1
        elif middle value > target value:
            set the left pointer equal to middle index + 1


    if you go traverse array and the value is not found:
        return -1
RESULTS:
    if the target integer is contained in the given array:
        return its index:
    else:
        return -1
'''

def binarySearch(array, target):
    pass

array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33

