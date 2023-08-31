'''
Link: https://leetcode.com/problems/valid-anagram/
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

'''
GIVEN:
    two strings
STEPS:
    SOLUTION 1: TIME AND SPACE COMPLEXITY: O(n)
        1. if the two lengths are not equal, return False
        2. create empty dictionary
        3. iterate through first string,
                if letter is not in the dictionary:
                    add it with 1 value
                else if letter is in dictionary:
                    increment its count by 1

        4. iterate through second string,
            if a letter is not in the dictionary:
                return False
            else if a letter is in the dictionay:
                decrement its count by 1

        if the sum of all the values in the dictionary is equal to 0:
            return True
        else
            return Flase

    SOLUTION 2: TIME COMPLEXITY: O(N), SPACE COMPLEXITY: O(1)
        1. sort the two given strings
        2. if the two sorted string are equal to each other, return True
            else return False

RETURN:
    return True, if they are anagrams
    else:
        return False

'''

def validAnagram(s,t):
    if len(s) != len(t):
        return False

    letterDictionary = {}

    for letter in s:
        if letter in letterDictionary:
            letterDictionary[letter] += 1
        else:
            letterDictionary[letter] = 1

    for letter in t:
        if letter not in letterDictionary:
            return False

        letterDictionary[letter] -= 1


    if sum(letterDictionary.values()) == 0:
        return True
    else:
        return False

s = "anagram"
t = "nagaram"
print(validAnagram(s,t))