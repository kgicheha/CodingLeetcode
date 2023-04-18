'''
Question Link:
https://www.algoexpert.io/questions/palindrome-check
'''
'''
Palindrome: a string that's written the same forward and backward
GIVEN:
    string
STEPS:
   initilize left pointer to 0
   initialize right pointer to the last character of the given string

   iterate through given string:
        if the character in the left pointer is equal to the character in the right pointer:
            increment left pointer by 1
            decrement right pointer by 1
        else:
            return False

    if it successfully goes through the iteration:
        return True

RESULT:
    return True if given string is a palindrome
    else:
        return False


TIME COMPLEXITY: O(n) || SPACE COMPLEXITY: O(1)

'''

def isPalindrome(string):
    lp = 0
    rp = len(string) - 1

    while lp <= len(string) - 1 and rp >= 0:
        if string[lp] == string[rp]:
            lp += 1
            rp -= 1
        else:
            return False
    return True




string = "abcdcba"
print(isPalindrome(string))