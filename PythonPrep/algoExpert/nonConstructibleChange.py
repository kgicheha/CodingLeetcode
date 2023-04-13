'''
Question Link:
https://www.algoexpert.io/questions/non-constructible-change

'''
'''
GIVEN:
    array of postive values that represent the coins you have.
STEPS:
    sort the given coins array
    initialize a vairable that keeps track of the sum of the coins as you iterate through given coins array
RESULT:
    return the minimum amount of change (minimum sum of money) you CANNOT create
'''

def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    currentCoinChange = 0

    for coin in coins:

        if coin > currentCoinChange + 1:
            return currentCoinChange + 1
        else:
            currentCoinChange += coin

    return currentCoinChange + 1

#  1, 1, 2, 3, 5, 7, 22

coins = [5,7,1,1,2,3,22]
print(nonConstructibleChange(coins))