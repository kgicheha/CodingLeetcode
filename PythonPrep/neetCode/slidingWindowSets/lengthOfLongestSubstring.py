def lengthOfLongestSubstring(s):

    seen = set()
    lp = 0
    rp = 0

    maxLength = 0

    while rp < len(s):
        if s[rp] in seen:
            seen.remove(s[lp])
            lp += 1

        else:
            seen.add(s[rp])
            rp += 1
            currentLength = rp - lp
            maxLength = max(currentLength, maxLength)

    return maxLength

s = "pwwkew"
print(lengthOfLongestSubstring(s))
'''
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''

'''
GIVEN:
    string
STEPS:

    initialize empty set

    intialize left pointer to 0
    initalize right pointer to 1

    initalize maxLength to 0 to keep track of the longest subString

    iterate given string while rp < length of string:

        if the character at right pointer is in set:
            remove character from set
            increment left pointer by 1
                this will resize the window

        else:
            add character to set
            calculate the length by from the left to the right pointer
            compare the current MaxLength with the length from the left to right pointers
                update the maxLength between the two

            increment right pointer by 1

    return maxLength
RESULT:

'''