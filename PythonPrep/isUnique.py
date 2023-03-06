'''
is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
'''


def isUnique(str):

    # USING ANOTHER DATA STRUCTURE
    # seen = set()

    # for s in str:
    #     if s not in seen:
    #         seen.add(s)
    #     else:
    #         return False

    # return True


    # WITHOUT USING ANOTHER DATA STRUCTURE

    sorted_str = sorted(str)

    for s in range(len(sorted_str) - 1):
        if sorted_str[s] == sorted_str[s + 1]:
            return False
    return True


print(isUnique("abcd10jk"))
print(isUnique("hutg9mnd!nk9"))

