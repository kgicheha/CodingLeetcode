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
# SOLUTION 2

def commonCharacters(strings):
    strings.sort()

    smallestStringSet = set(strings[0])
    uniqueCharacters = {}

    for string in strings:
        checkCommonCharacters(smallestStringSet, string, uniqueCharacters)

    print(uniqueCharacters)

def checkCommonCharacters(smallestStringSet, string, uniqueCharacters):

    currentStringSet = set(string)

    print(currentStringSet)

    for char in currentStringSet:
        if char in smallestStringSet:
            uniqueCharacters[char] = 1
        # else:
        #     del uniqueCharacters[char]



'''
SOLUTION 1

def commonCharacters(strings):
    result = []
    charDictionary = {}

    strings.sort()
    print(strings)

    for string in strings:
        charCheck(string, charDictionary)

    print(charDictionary)
    for char, count in charDictionary.items():
        if count == len(strings):
            result.append(char)

    return result

def charCheck(string, charDictionary):

    uniqueCharacters = set(string)

    for char in uniqueCharacters:
        if char not in charDictionary:
            charDictionary[char] = 1

        else:
            charDictionary[char] += 1

'''

strings = ["bcd", "cbaccd", "abc"]
print(commonCharacters(strings))