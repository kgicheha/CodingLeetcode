import math

'''
Given a list of numbers with an odd number of elements, find the median?
    Median is the value separating the higher half from the lower half of a data sample
    formula = (high + low) / 2
'''

def findMedian(arr):
    arr.sort()
    # SOLUTION 1
    medium_index = (arr[0] + (len(arr)-1)) // 2
    result = arr[medium_index]
    print(result)

    # SOLUTION 2
    # median = arr[len(arr) // 2]

    # return median


arr =[5,3,1,2,4]
findMedian(arr)