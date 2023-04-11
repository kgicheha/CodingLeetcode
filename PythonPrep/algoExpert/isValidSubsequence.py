'''
Question:
https://www.algoexpert.io/questions/validate-subsequence
'''
'''
GIVEN:
    2 non-empty arrays
STEPS:
    create two pointers:
        1. keeps track of where you are in the 1st array
        2. keeps track of where you are in the sub sequence array

    traverse through the two array, while the two pointers are less than the len of the array:
        if the current number in the 1st array is equal to the current number in the subsquence array:
            increment the sequence pointer by 1

        else increment the pointer of the array index by 1 as you're searching for the number that equal to the current number in the sequence array

    if the sequence index is equal to the length of the sequence array, return True
        this means that all the numbers in the sequence array are in the 1st array.


RETURN
    return True, if the sequence is in the first array
    else return False

TIME COMPLEXITY: O(N) --> have to traverse entire array
SPACE COMPLEXITY: O(1) --> we dont have to create any new data structure
'''

def isValidSubsequence(array, sequence):
    arrIndex = 0
    seqIndex = 0

    # USING WHILE LOOP
    # while arrIndex < len(array) and seqIndex < len(sequence):

    #     if array[arrIndex] == sequence[seqIndex]:
    #         seqIndex += 1

    #     arrIndex += 1
    # return seqIndex == len(sequence)

    # USING FOR LOOP
    for value in array:
        if seqIndex == len(sequence):
            break
        if sequence[seqIndex] == value:
            seqIndex += 1

    return seqIndex == len(sequence)


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 22, 25, 6, -1, 8, 10]
print(isValidSubsequence(array, sequence))