'''
Given a list of unsorted integers, ,
find the pair of elements that have the smallest absolute difference between them.
If there are multiple pairs, find them all.
'''

'''
GIVEN:
    array of unsorted numbers
STEPS:
RETURN:
    return an array of the pair of numbers, that has the smallest absolute difference betweent them
'''

def closestNumbers(arr):
    arr.sort()
    print(arr)

arr = [5,2,3,4,1]
closestNumbers(arr)