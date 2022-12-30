'''
A person wants to determine the most expensive computer keyboard
and USB drive that can be purchased with a give budget.
Given price lists for keyboards and USB drives and a budget,
find the cost to buy them.
If it is not possible to buy both items, return -1 .

'''

'''
Example 1
b = 60
keyboards = [40,50,60]
drives = [5,8,12]

The person can buy a  40 keyboard + 12 USB drive = 58
or
50 keyboard + 8 USB drive = 58
return 58 because its the more expensive option
'''

'''
GIVEN: array of keyboard prices, array of USB drive prices, and a target price
STEPS:
    create empty object to store the differences
    iterate first array
        if the current value is <= target bugdet
            get the difference between the current number in the keyboard array and target price
            store the difference in the empty object
    iterate second array
        if the current value is

RETURN: the sum of the two options that closest to the target price budget
'''


def getMoneySpent(keyboards, drives, b):
    # BRUTE FORCE
    max_spent = 0

    for i in range(len(keyboards)):
        for j in range(len(drives)):
            cost = keyboards[i] + drives[j]
            if (cost <= b):
                if (max_spent == 0):
                    max_spent = cost
                elif (cost > max_spent):
                    max_spent = cost

    if (max_spent == 0):
        print(-1)
    else:
        print(max_spent)
