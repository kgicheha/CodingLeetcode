
from collections import defaultdict
'''
49. Group Anagrams
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the
letters of a different word or phrase,
typically using all the original letters exactly once.

'''

'''
EXAMPLE 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

'''

'''
GIVEN: array of strings
STEPS:
    create empty dictionary
    loop through given array
        sort every word in the array
        check to see if the sorted word is in the array

        if sorted word is not dictionary, add it to the dictionary
            the key will be the sorted word
            the value will be the given word

        if the sorted word is in the dictionary:
                append the given word as the value of the sorted word

        create empty output array
        loop through the dictionary
            append all the values to the output array
RETURN: array of arry of groups anagrams

'''

def groupAnagrams(strs):

    # lookup = defaultdict(list)
    lookup = {}

    for word in strs:
            sorted_word = sorted(word)
            key = "".join(sorted_word)

            if key not in lookup:
                lookup[key] = [word]
            else:
                lookup[key].append(word)

    output = []
    for item in lookup.values():
        output.append(item)

    return output


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))