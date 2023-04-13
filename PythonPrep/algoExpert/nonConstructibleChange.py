'''
Question Link:
https://www.algoexpert.io/questions/non-constructible-change

'''
'''
GIVEN:
    array of postive values that represent the coins you have.
STEPS:
RESULT:
    return the minimum amount of change (minimum sum of money) you CANNOT create
'''

def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    change = 0

    for value in coins:
        curSum = change + value
        if change < curSum:
            change += value
        # elif change

    print(change)


coins = [5,7,1,1,2,3,22]
print(nonConstructibleChange(coins))