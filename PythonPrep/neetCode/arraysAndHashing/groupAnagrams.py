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

        create empty dictionary with list as its argument

        iterate through given array:
            for each string in the array:
                sort the character
                join the character
                add the  sortedCharacter to the dictionary with the unsorted version as its value

        return the result dictionary



    STRATEGY 2:
        create empty dictionary with lists as its argument

        iterate through given array:
            itialize array with 26 Os, to represent the 26 letters in the alphabet
                this will keep count of the character that appear in each string

            for each character in a string:
                increment the count by 1 where character appears in the alphabet


            append the tuple of the character count with the string as its value

        return the result array


RESULTS:

'''