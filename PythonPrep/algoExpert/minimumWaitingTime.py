'''
Question Link:
algoexpert.io/questions/minimum-waiting-time
'''

'''
GIVEN:
    non-empty array of positive integers
    ALLOWED TO MUTUTATE THE INPUT ARRAY
STEPS:
    # sort the given array


    initialize variable that keeps track of the wait time

    traverse sorted array:

RESULTS:
    return the minimum amount of total waiting time for all of the queries


Time Complexity -->O(n log n) + n || Space Complexity --> O(1)
'''

def minimumWaitingTime(queries):

    queries.sort()

    totalWaitTime = 0

    for index, duration in enumerate(queries):
        queriesLeft = len(queries) - (index + 1)

        totalWaitTime += duration * queriesLeft

    return totalWaitTime


queries = [3, 2, 1, 2, 6]
print(minimumWaitingTime(queries))

# [1, 2, 2, 3, 6]