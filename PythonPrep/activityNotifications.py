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
    create variable that keeps track of total count
        initialize it to 0
    create left pointer and initialize it to 0
    create right pointer and initialize it to d
    create a variable of where you will begin your loop
        d + 1


    loop though given array
        calc the median of the numbers from left pointer to right pointer
            median = len(array) // 2
        calc the threshold
            threshold = 2 * median

        if the current number >= threshold:
            increment counter by 1

        increment left pointer by 1
        increment right pointer by 1
        increment cur number by 1
RESULT:
    return the number of notices sent

'''
def activityNotifications(expenditure, d):
    # Write your code here

    total_count = 0
    lp = 0
    rp  = d - 1
    cur_num = d



    while cur_num < len(expenditure):

        trail_day_range = sorted(expenditure[lp:cur_num])

        # median = (trail_day_range[lp] + trail_day_range[rp]) // 2
        median = trail_day_range[d // 2]

        threshold = 2 * median

        if expenditure[cur_num] >= threshold:
            total_count += 1


        cur_num += 1
        lp += 1
        rp += 1

    print(total_count)


expenditure = [1, 2, 3, 4, 4]
d = 4
activityNotifications(expenditure, d)