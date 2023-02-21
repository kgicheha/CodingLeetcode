'''
Given a string and a positive number k,
find the longest substring of the string containing
k distinct characters.
If k is more than the total number of distinct characters
in the string,
return the whole string.

'''

'''
GIVEN:
    1. string
    2. k postive number
STEPS:
    if k is > than the total number of distinct characters
        return the whole string

    intialize start and end indeces to 0

    initialize empty set

    while endIndex is valid:
        expand window by increasing endIndex
        while condition is NOT true:
            shrink window by increasing startIndex

            keep track of the result

    return the result



RESULT:
    return the longest substring of the string containing k distinct characters


'''

def longestDistinctSubString(str, k):
    print(str)

    startIdx, endInx = 0 ,0

    window = set()

    freq = []

    # maintains the sliding window boundaries
    low, high = 0,0

    while endInx < len(str):

        window.add(str[right])

        while

        print(window)
        right += 1




str = "abcbdbdbbdcdabd"
k = 2

longestDistinctSubString(str,k)