'''
Question Link:
https://www.algoexpert.io/questions/common-characters
'''

'''
GIVEN:
    array of strings
STEPS:
    intitialize empty dictionary
    initialize empty result array

    traverse each string:
        if character is not dictionary:
            add it to dictionary with 1 value
        else:
            increment the value of the character in the dictionary


    if value of the character in the dicitonary is equal to the length of the given array:
        add it to the the result array
RESULTS:
    array of characters that are common to all the strings

'''

def commonCharacters(strings):
    result = []
    charDictionary = {}
    for string in strings:
        charCheck(string, charDictionary)

    for char, count in charDictionary.items():
        if count == len(string):
            result.append(char)

    return result

def charCheck(string, charDictionary):

    for char in string:
        if char not in charDictionary:
            charDictionary[char] = 1

        charDictionary[char] += 1

strings = ["abc", "bcd", "cbaccd"]
print(commonCharacters(strings))