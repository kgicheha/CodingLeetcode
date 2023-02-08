'''
Two strings are anagrams of each other if the letters of one string
can be rearranged to form the other string.

Given a string, find the number of pairs of substrings of the string
that are anagrams of each other.
'''

'''
GIVEN:
    1. string
STEPS:
RESULT:
    the number of unordered anagrammatic pairs of substrings in s
'''

def sherlockAndAnagrams(s):

    all_letters = {}
    all_combos = []

    lp = 0
    rp = 0

    for lp in range(len(s)):
        while rp <= len(s):
            print(s[lp:rp])
            all_combos.append(s[lp:rp])
            rp += 1



    print(all_combos)

    for i in s:
        if i not in all_letters:
            all_letters[i] = 1
        else:
            all_letters[i] += 1

    # print(all_letters)

    ana_array = []

    for i in all_letters:
        if all_letters[i] % 2 ==0:
            ana_array.append(i)

    # print(ana_array)

sherlockAndAnagrams("mom")