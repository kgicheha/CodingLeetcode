'''
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals,
and return an array of the non-overlapping intervals
that cover all the intervals in the input.
'''

'''
EXAMPLE 1
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


EXAMPLE 2
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

'''

'''
GIVEN: 2d array
STEPS:
    create result variable and set it as an empt array
    sort the arrays based on the  values at index 0

    loop through sorted array
        if result is not empty AND the value at the index 0 of the current interval is less than the value at index 1 of the last interval in the result array
            set the value at the index 1 of the last interval in the result are
                as the max value between itself and the value at index 1 of the current interval

        else
            append the current interval to the result array


    RETURN result

TIME COMPLEXITY: 0(n)
SPACE COMPLEXITY: 0(N)
'''


def merge(intervals):
    result = []

    for interval in sorted(intervals, key=lambda x:x[0]):
        if result and interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)

    print(result)

intervals = [[1,4],[4,5]]
intervals2 = [[1,3],[2,6],[8,10],[15,18]]
merge(intervals)
merge(intervals2)