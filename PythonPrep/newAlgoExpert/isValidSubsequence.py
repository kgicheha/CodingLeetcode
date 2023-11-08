def isValidSubsequence(array, sequence):

    arrayIdx = 0
    sequenceIdx = 0

    while arrayIdx < len(array) and sequenceIdx < len(sequence):
        if array[arrayIdx] == sequence[sequenceIdx]:
            sequenceIdx += 1

        arrayIdx += 1

    return sequenceIdx == len(sequence)


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))


'''
Link: https://www.algoexpert.io/questions/validate-subsequence
'''
'''
GIVEN:
    2 non-empty array
STEPS:

    initialize pointer 1 equal to 0 --> will be used for given array
    initialize pointer 2 equal to 0 --> will be used for sequence array

    iterate given array:
        if number at pointer 1 is equal to number at pointer 2:
            increment pointer 2 by 1



        increment pointer 1 by 1

    return pointer2 == length of sequence array:
        will return True if the entire sequence has been traversed
        else will return False


    return True

RESULT:
    return True if the sequence is a subset
    else return False

'''

