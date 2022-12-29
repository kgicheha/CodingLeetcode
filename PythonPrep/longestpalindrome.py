import math

'''
5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.
'''
'''
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
'''

'''
GIVEN: string

RETURN longest substring that is a palindrome(can read the same forward and backward)

'''

def longestpal(str):
    start_point = math.ceil((len(str) + 1) / 2)

    for i in range(0, start_point):

        print(str[i])


longestpal("cbbd")