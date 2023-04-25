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
    initialize two pointers
        left pointer starts at 0
        right pointer starts at the last element of the array

    initialize variable that keeps track of the wait time
RESULTS:
    return the minimum amount of total waiting time for all of the queries
'''

def minimumWaitingTime(queries):

    queries.sort()
    print(queries)

    min_wait_time = 0

    for i in range(1,len(queries)):

        min_wait_time += queries[i - 1]

    return min_wait_time

queries = [3, 2, 1, 2, 6]
print(minimumWaitingTime(queries))

# [1, 2, 2, 3, 6]