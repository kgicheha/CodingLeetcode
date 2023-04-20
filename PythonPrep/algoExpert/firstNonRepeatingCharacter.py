'''
Question Link:
https://www.algoexpert.io/questions/first-non-repeating-character
'''

'''
GIVEN:
    string of lowercase English-alphabet letters
STEPS:

    SOLUTION 1:
        initialize empty dictionary

        traverse given string:
            if character is not in dictionary:
            add character to dictionary with 1 value
            else:
                increment its value by 1

        get character from dictionary that has value of 1

        traverse given string
            if currentCharacter == character from the dictionary:
                return its index

        return -1 if no non-repeating character is found


    RESULT:
        return the index of the string's first non-repeating character
        else:
            return -1 if string doesn't have non-repeating characters

        Time Complexity 0(n) || Space Complexity O(1) -> because at most you'll have 26 letters in your dictionary

'''

# SOLUTION 1
def firstNonRepeatingCharacter(string):

    seen = {}

    for char in string:
        if char not in seen:
            seen[char] = 0
        else:
            seen[char] += 1

    print(seen)
    nonRepeatChar = ''

    for char,count in seen.items():
        if count == 0:
            nonRepeatChar = char
            break

    for char in range(len(string)):
        if string[char] == nonRepeatChar:
            return char

    return -1

string = "abcdcaf"
print(firstNonRepeatingCharacter(string))

