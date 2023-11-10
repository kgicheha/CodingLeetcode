from collections import defaultdict

def groupAnagrams(strs):
    # STRATEGY 1:

    result = defaultdict(list)

    for s in strs:
        print(sorted(s))
        sortedChar = "".join(sorted(s))

        result[sortedChar].append(s)

    return result

    # STRATEGY 2
    # result = defaultdict(list)

    # for s in strs:
    #     count = [0] * 26

    #     for char in s:
    #         count[ord(char) - ord("a")] += 1

    #     result[tuple(count)].append(s)


    # return result.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
'''
Link:
https://leetcode.com/problems/group-anagrams/

'''

'''
An Anagram is a word or phrase formed by rearranging
the letters of a different word or phrase,
typically using all the original letters exactly once.

GIVEN: array of strings
STEPS:

    # STRATEGY 1: sorting the characters --> TIME COMPL = O(m*n + nlogn) , SPACE COMPL  = O(n)

        import defaultdict from collections

        create empty dictionary

        iterate through given array:
            for each array:
                sort the character
                join the character
                add the  sortedCharacter to the dictionary with the unsorted version as its value

        return the result dictionary

RESULTS:

'''