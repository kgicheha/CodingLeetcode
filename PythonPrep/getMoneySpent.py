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

def getMoneySpent(keyboard, drives, b):
