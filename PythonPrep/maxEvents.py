'''
1353. Maximum Number of Events That Can Be Attended
You are given an array of events
where events[i] = [startDayi, endDayi].
Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d
where startTimei <= d <= endTimei.
You can only attend one event at any time d.

Return the maximum number of events you can attend.
'''

'''
EXAMPLE 1
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

'''

'''
GIVEN:
    2D array --> index 0: the start day, index 1: end day
STEPS:
    sort by the end date (index 1)
    create variable that stores the maxEvents
        initialize it to 0
RESULTS: max number of events you can attend
'''

def maxEvents(events):

    events.sort(key = lambda x: x[1])

    maxEvents = 0
    return events





# events= [[1,2],[2,3],[3,4],[1,2]]
events= [[ 1,4],[4,4],[2,2],[3,4], [1,1]]
print(maxEvents(events))