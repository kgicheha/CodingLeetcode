''''
GIVEN:
    given 2 sorted arrays of integers

STEPS:


    # Time Complexity: O(n log n) || Space Complexity = O(n + m)
    BRUTE FORCE:
        concat the two arrays
        sort

    OPTIMIZED:
        initialize empty results array
        initialize pointer1 to arry1[0]
        initialize pointer2 to array2[0]

        while pointer1 <= length(array1) - 1 and pointer2 <= len(array2) - 1 :

            if the value at pointer1 < value at pointer2:
                add value at pointer1 to results array
                increment pointer1 by 1
            elif the value at pointer1 > value at pointer2:
                add value at pointer2 to results array
                increment pointer2 by 1
            else:
                add value at pointer1 to results array
                add value at pointer2 to results arry
                increment pointer1 by 1
                increment pointer2 by 1

RESULTS:
    sorted array consisting of the 2 given arrays
'''

'''
EXAMPLE:
array1 = [2, 3, 5]
array2 = [3, 4, 5]
'''

def mergeArrays(array1, array2):

    # mergedArray = array1 + array2
    # mergedArray.sort()
    # return mergedArray

    results = []
    pointer1 = 0
    pointer2 = 0

    while pointer1 <= len(array1) - 1 and pointer2 <= len(array2) - 1:

        if array1[pointer1] < array2[pointer2]:
            results.append(array1[pointer1])
            pointer1 += 1

        elif array1[pointer1] > array2[pointer2]:
            results.append(array2[pointer2])
            pointer2 += 1
        else:
            results.append(array1[pointer1])
            results.append(array2[pointer2])
            pointer1 += 1
            pointer2 += 1

    return results


array1 = [2, 3, 5, 7]
array2 = [1, 2, 3, 4, 5]

print(mergeArrays(array1, array2))
# [2, 3, 5, 3, 4, 5]

# Time Complexity: O(n log n) || Space Complexity = O(n + m)

'''
p1: 0
p2: 0
results = [1]

p1: 0
p2: 1
results = [1, 2 , 2]

p1: 1
p2: 2
results = [1, 2 , 2, 3, 3]

p1: 2
p2: 3
results = [1, 2 , 2, 3, 3, 4]

p1: 2
p2: 4
results = [1, 2 , 2, 3, 3, 4, 5]


'''