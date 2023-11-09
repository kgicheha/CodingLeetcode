def isAnagram(s,t):

    # STRATEGY 1
    # if len(s) != len(t):
    #     return False

    # charS, charT= {}, {}

    # for char in range(len(s)):
    #     charS[s[char]] = 1 + charS.get(s[char], 0)
    #     charT[t[char]] = 1 + charT.get(t[char], 0)

    # for char in charS:
    #     if charS[char] != charT.get(char, 0):
    #         return False

    # return True

    # STRATEGY 2

    s = sorted(s)
    t = sorted(t)

    if s == t:
        return True
    return False
s = "aacc"
t = "ccac"
print(isAnagram(s,t))
'''
Link: https://leetcode.com/problems/valid-anagram/
'''

'''

An Anagram is a word or phrase formed by rearranging
the letters of a different word or phrase,
typically using all the original letters exactly once.
GIVEN:
    two strings
STEPS:

    # STRATEGY 1: using dictionaries --> TIME AND SPACE COMPLEX : 0(n)

        create 2 empty dictionaries,
            each will store the character count of the each given string

        iterate through the first string:
            for each character:
                if character is not in the dictionary:
                    add it to the dictionary
                else:
                    increment its count by 1


        iterate though the 2nd string:
        for each character:
                if character is not in the dictionary:
                    add it to the dictionary
                else:
                    increment its count by 1


        if the value of character in the first dictionary is not equal to the value in the 2nd dictionary
            return False

        return True


    STRATEGY 2: sort the 2 strings, TIME Complexity O(nlogn), SPACE Complexity: O(1)

RESULTS:
    return True if t string is an anagram of s string
    else:
        return False

'''