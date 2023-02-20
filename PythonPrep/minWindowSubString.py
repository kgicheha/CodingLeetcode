import collections
import sys

'''
Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character in t
(including duplicates) is included in the window.
If there is no such substring, return the empty string ""
'''
'''
GIVEN:
    two strings
STEPS:
    edge case: if t is empty, return ''

    TWO POINTER APPROACH
    intialize left and right pointer equal to 0

RESULT:


'''
def minWindowSubString(s,t):
    if t == '':
        return ''

    left, right = 0 , 0

    minimum = sys.maxsize
    counter_t = collections.Counter(t)
    counter_search = collections.defaultdict(int)
    count = 0
    minimum_window = ""

    while right <



s = "ADOBECODEBANC"
t = "ABC"


minWindowSubString(s,t)