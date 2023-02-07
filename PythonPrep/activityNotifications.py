'''
Given the number of trailing days  and a client's total daily
expenditures for a period of  days, determine the
number of times the client will receive a notification over all  days.
'''

'''
If the amount spent by a client on a particular
day is greater than or equal to 2X the client's median spending for a trailing
number of days, they send the client a notification about potential fraud.
'''

'''
GIVEN:
    1. array of digits
    2. the number of trailing days

STEPS:

RESULT:
    return the number of notices sent

'''
def activityNotifications(expenditure, d):
    # Write your code here
    expenditure.sort()

    median = expenditure[len(expenditure) // 2]





expenditure = [10,20,30,40,50]
d=3
activityNotifications(expenditure, d)