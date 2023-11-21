def permutions(array):
    if len(array) == 0:
        return []

    # base case
    if len(array) == 1:
        return [array[:]]

    for i in range(len(array)):
        num = array.pop(0)

        perms = self.permutations(array)

        for perm in perms:
            perm.append(num)
            result.append(perm)
        array.append(num)


array = [1,2,3]

print(permutions(array))

'''
GIVEN:
    array of unique integers
STEPS:
RESULTS:
    return all the permutations of those integers

    if input is empty,
        return an empty array
'''