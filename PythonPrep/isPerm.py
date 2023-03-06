'''
Check Permutation:
Given two strings, write a method to decide if one is a permutation of the
other.

Permutation of a string is another string that contains same characters,
only the order of characters can be different. For example, “abcd” and “dabc”
are Permutation of each other.

'''

def isPermutation(str1, str2):

    if len(str1) != len(str2):
        return False


    #SOLUTION 1: USING OBJECT
    # TIME COMPLEXITY: O(n + m)
    # SPACE COMPLEXITY: O(n)

    # seen = {}

    # for i in range(len(str1)):
    #     if str1[i] not in seen:
    #         seen[str1[i]] = 1
    #     else:
    #         seen[str1[i]] += 1

    # print(seen)

    # for i in range(len(str2)):
    #     if str2[i] in seen:
    #         seen[str2[i]] -= 1
    #     else:
    #         return False

    # if sum(seen.values()) == 0:
    #     return True
    # else:
    #     return False



    # SOLUTION 2: WITHOUT USING OBJECT
    # TIME COMPLEXITY = O(n)
    # SPACE COMPLEXITY = O(1)

    sorted_str1 = sorted(str1)
    joined_str1 = "".join(sorted_str1)

    sorted_str2 = sorted(str2)
    joined_str2 = "".join(sorted_str2)

    combined_str = sorted(joined_str1 + joined_str2)
    print(combined_str)



# print(isPermutation("test", "rest"))
print(isPermutation("test", "test"))


