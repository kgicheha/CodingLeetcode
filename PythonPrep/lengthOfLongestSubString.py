'''
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring
without repeating characters.
'''

'''
EXAMPLE 1
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

EXAMPLE 2
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

'''

'''
GIVEN: string
STEPS:
    create SET that will store the characters
    create left pointer initialized to 0
    create result and initialize it to 0
    iterate string
        while character of the right pointer is in the SET
            remove character at lp from SET
            update the sliding window
                increment left pointer by 1
        add the character in the right pointer to the SET
        update the result with the max number
            between whats currently stored in the result and right pointer - the left pointer + 1
    return result
Return: length of longest substring without repeating characters

'''
def lengthOfLongestSubstring(s: str):

    charSet = set()
    lp = 0
    res = 0

    for rp in range(len(s)):
        while s[rp] in charSet:
            charSet.remove(s[lp])
            lp += 1

        charSet.add(s[rp])

        res = max(res, rp - lp + 1)
    return res

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))