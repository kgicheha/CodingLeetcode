'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters
include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

'''
EXAMPLE 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

'''
GIVEN: string
STEPS:
    TWO POINTER SOLUTION
    set left pointer equal to the first index
    set the right pointer equal to the last index

    while left pointer < right pointer:
        while left pointer < right pointer and character at left pointer is not an alphabet or number:
            increase left pointer by 1
        while left pointer < right pointer and character at right pointer is not an alphabet or number:
            decrement right pointer by 1

        if the character at the left pointer is not equal to the character at the right pointer:
            return False

        else:
            increment left pointer by 1
            decrement right pointer by 1

        return True

RESULT: return true if string is a palindrome, else return false

'''

def isPalindrome(s):
    lp = 0
    rp = len(s) - 1

    while lp < rp:
        while lp < rp and not s[lp].isalnum():
            lp += 1
        while lp < rp and not s[rp].isalnum():
            rp += 1

        if s[lp].lower() != s[rp].lower():
            return False

        lp +=1
        rp -=1
        return True



s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
