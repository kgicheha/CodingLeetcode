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

def maxEvents(events):
    print(events)