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
'''

def isValidSubsequence(array, sequence):
    lp = 0
    rp = 0

    while lp <= len(sequence):
        if sequence[lp] in array:
            lp += 1
    return True

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 22, 25, 6, -1, 8, 10]
isValidSubsequence(array, sequence)