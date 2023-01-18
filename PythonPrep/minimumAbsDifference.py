'''
1200. Minimum Absolute Difference
Given an array of distinct integers arr,
find all pairs of elements with the minimum absolute difference
of any two elements.

Return a list of pairs in ascending order(with respect to pairs),
each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements
in arr

'''

'''
EXAMPLE 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1.
List all pairs with difference equal to 1 in ascending order.
'''
'''
GIVEN: given array of DISTINT integers
STEPS:
    sort the given array in asending order
    create empty list that will be used to store the result
    create a variable that will store the minimum difference
        initialize it to the difference between the first and second value

    loop through sorted array
        to find the lowest difference between the numbers
        if you find the lowerest difference save it into the "minimum difference" variable

    loop through array again
        if you find a pair that has the same difference as the one that stored in the "minimum difference" variable
            add the pair to the result array

        return the result array


RESULT: return a list of pairs in ASCENDING order
            of the pairs with the minimum absolute difference

'''
def minimumAbsDifference(arr):

    arr.sort()

    res = []
    min_diff = arr[1] - arr[0]

    for i in range(1, len(arr)):
        min_diff = min(arr[i] - arr[i-1], min_diff)
        print(min_diff)

    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == min_diff:
            pair = [arr[i-1], arr[i]]
            res.append(pair)

    return res


arr = [4,2,1,3]
print(minimumAbsDifference(arr))