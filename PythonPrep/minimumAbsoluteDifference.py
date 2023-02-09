'''
Given an array of integers,
find the minimum absolute difference between any two elements in the array.
'''
'''
GIVEN:
    array of integers
STEPS:
    create vairable that stores the min abs difference

    loop through array
        get the difference
RESULT:
    return the mininum absolute difference between any two elements

'''

def minimumAbsoluteDifference(arr):
    arr.sort()

    min_dif = abs(arr[0] - arr[1])

    for i in range(len(arr)-1):
        cur_diff = abs(arr[i] - arr[i+1])
        min_dif = min(min_dif, cur_diff)

    print(min_dif)


arr = [3,-7,0]
minimumAbsoluteDifference(arr)