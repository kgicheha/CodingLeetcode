def isPalindrome(s):
    # SOLUTION 1
    # newString = ""

    # for char in s:
    #     if char.isalnum():
    #         newString += char.lower()


    # return newString == newString[::-1]

    lp = 0
    rp = len(s) - 1


    while lp < rp:
        while lp < rp and not alphaNum(s[lp]):
            lp += 1

        while rp > 1 and not alphaNum(s[rp]):
            rp -= 1

        if s[lp].lower() != s[rp].lower():
            return False

        lp += 1
        rp -= 1

    return True


def alphaNum(char):
    return (ord('A') <= ord(char) <= ord('Z')
        or (ord('a') <= ord(char) <= ord('z'))
        or (ord('1') <= ord(char) <= ord('9'))
        )

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

'''
Link: https://leetcode.com/problems/valid-palindrome/
'''

'''
A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters,
 it reads the same forward and backward.

GIVEN:
    a string
STEPS:
    STRATEGY 1: TIME COMPLEXITY: O(n), SPACE COMPLEXITY: O(n)
        Create an empty string called 'newString' to store our cleaned up version of the input string.

        iterate through given string:
            if the current character is alphanumeric:
                add the lower case character to the newString

        return True if the newString is the same in as it and when its reversed


    STRATEGY 2: creating helper function

        create helper function to check whether character is alphanumeric

        initialize left pointer to 0
        initialize right pointer to last element


        iterate through given string while left pointer is less than right pointer:

            while the left pointer is less the right:
                check to see if the character is alphanumeric by passing into the helper function:
                    if it is:
                        increment the left pointer by 1

            while the right pointer is more than 1:
                check to see if the character is alphanumerica by passing into the helper function:
                    if it is:
                        decrement right pointer by 1

        if the lower case version of the character at the left pointer is not equal to the lowercase verson of the character at the right pointer:
            return False


    return True
        if the loop completes

RESULTS:
'''