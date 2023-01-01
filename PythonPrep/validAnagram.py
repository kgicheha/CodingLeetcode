'''
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s,
 and false otherwise.

An Anagram is a word or phrase formed by
rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

'''

'''
EXAMPLE 1:
Input: s = "anagram", t = "nagaram"
Output: true

EXAMPLE 2:
Input: s = "rat", t = "car"
Output: false
'''

'''
GIVEN: string
STEPS:
    BASE CASE:
        if the lengths are not the same,
            return False

    create two empty dictionaries
        these will store the frequency count of the characters in both the given strings
    iterate strings
        if character is not in dict,
            add it and set its count to 1
        if it is in dict
            increase count by 1
    compare the count of the characters in the dictionary
        if the count are not the same,
            return false
    return True
        means that the string have passed the tests
RESULT: return true if s is an anagram of t, else return false

'''

def isAnagram(s,t):
    # SOLUTION 1: using hasMap
        # TIME and SPACE Complexities: O(n)
            # have to iterate and save the characters in the strings

    # if len(s) != len(t):
    #     return False

    # countS, countT = {}, {}

    # for i in range(len(s)):
    #     countS[s[i]] = 1 + countS.get(s[i], 0)
    #     countT[t[i]] = 1 + countT.get(t[i], 0)

    # for c in countS:
    #     if countS[c] != countT.get(c, 0):
    #         return False

    # return True


    # SOLUTION 2: sort characters
        # TIME COMPLEXITY: O(n)
        # SPACE COMPLEXITY: O(1)
    return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"
print(isAnagram(s,t))

