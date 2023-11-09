def minWindow(s, t):
    if len(t) == 0:
        return ""

    countT, currentWindow = {}, {}

    for char in t:
        if char not in countT:
            countT[char] = 0

        countT[char] += 1


    have = 0
    need = len(countT)

    result = [-1, -1]
    resultLength = float("inf")

    lp = 0

    for rp in range(len(s)):
        if currentWindow[s[rp]] not in currentWindow:
            currentWindow[s[rp]] = 0

        currentWindow[s[rp]] += 1

        if s[rp] in countT and currentWindow[s[rp]] == countT[s[rp]]:
            have += 1


        while have == need:
            # update result
            if (rp + lp - 1) < resultLength:
                result = [lp, rp]
                resultLength = (rp - lp + 1)

            # pop from left of window
            currentWindow[s[lp]] -= 1

            if s[lp] in countT and  currentWindow[s[lp]] < countT[s[lp]]:
                have -= 1

            lp += 1

    lp, rp = result
    return s[lp:rp+1] if resultLength != float("inf") else  ""

s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s, t))



'''
Link: https://leetcode.com/problems/minimum-window-substring/
'''

'''
GIVEN:
    two strings

STEPS:

    if string t is emptry, return empty string

    initialize two empty hashmaps:
        1st one will be used to store the characters in the T string
        2nd one will be used to store the character in the current window as we iterate through s string


    iterate through t string:
        if the current character doesn't exist in the hashmap:
            add it with a 1 count

        else if the character exists:
            increment the count by 1

    initialize a variable to store the length of characters you have while you iterate s string
    initialzie a variable to store the length of character you need


RESULT:

'''