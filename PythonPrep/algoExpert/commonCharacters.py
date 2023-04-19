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
        initialize empty set to store the unique characters in each string

        add the unique characters to the set

        for each character in the set:

            if character is not dictionary:
                add it to dictionary with 1 value
            else:
                increment the value of the character in the dictionary


    for each item in the dictionary:
        if value of the character in the dicitonary is equal to the length of the given array:
            add it to the the result array

    return the results array
RESULTS:
    array of characters that are common to all the strings

'''

def commonCharacters(strings):
    result = []
    charDictionary = {}

    for string in strings:
        charCheck(string, charDictionary)

    print(charDictionary)
    for char, count in charDictionary.items():
        if count == len(strings):
            result.append(char)

    return result

def charCheck(string, charDictionary):

    seen = set()

    for char in string:
        if char not in seen:
            seen.add(char)

    for char in seen:
        if char not in charDictionary:
            charDictionary[char] = 1

        else:
            charDictionary[char] += 1

strings = ["abc", "bcd", "cbaccd"]
print(commonCharacters(strings))