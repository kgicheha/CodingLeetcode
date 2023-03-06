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

    str.sort()

    print(str)






isUnique("abcd10jk")
isUnique("hutg9mnd!nk9")

