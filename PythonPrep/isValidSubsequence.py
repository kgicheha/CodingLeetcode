'''
Question:
https://www.algoexpert.io/questions/validate-subsequence
'''
'''
GIVEN:
    2 non-empty arrays
STEPS:
RETURN
    return True, if the sequence is in the first array
    else return False

TIME COMPLEXITY: O(N) --> have to traverse entire array
SPACE COMPLEXITY: O(1) --> we dont have to create any new data structure
'''

def isValidSubsequence(array, sequence):
    arrIndex = 0
    seqIndex = 0

    while arrIndex < len(array) and seqIndex < len(sequence):

        if array[arrIndex] == sequence[seqIndex]:
            seqIndex += 1

        arrIndex += 1
    return seqIndex == len(sequence)

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 22, 25, 6, -1, 8, 10]
print(isValidSubsequence(array, sequence))