def getPermutations(array):

    res = []

    # base case
    if (len(array) == 1):
        return [array.copy()]

    for i in range(len(array)):
        n = array.pop(0)
        perms = getPermutations(array)


        for perm in perms:
            perm.append(n)

        res.extend(perms)
        array.append(n)

    return res

array = [1,2,3]
# Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
print(getPermutations(array))

'''
GIVEN:
    array of unique integers
STEPS:


RESULTS:
    return an array of all permutations of those integers

    if the array is empty, return empty array
'''