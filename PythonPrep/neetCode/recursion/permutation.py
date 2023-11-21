def permutations(array):
    if len(array) == 0:
        return []

    result = []
    backtrack(0, array, result)
    return result

def backtrack(i, array, result):
    # base case
    if i == len(array)-1:
        result.append(array[:])

    else:
        # recursion
        for j in range(i,len(array)):
            array[i], array[j] = array[j], array[i]
            backtrack(i+1, array, result)
            array[i], array[j] = array[j], array[i]


array = [1,2,3]

print(permutations(array))

'''
GIVEN:
    array of unique integers
STEPS:
RESULTS:
    return all the permutations of those integers

    if input is empty,
        return an empty array
'''