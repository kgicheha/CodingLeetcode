def maxProfit(prices):
    lp = 0
    rp = 1

    maxProfit = 0

    while rp < len(prices):

        if prices[lp] < prices[rp]:
            currentProfit = prices[rp] - prices[lp]
            maxProfit = max(currentProfit, maxProfit)

        else:
            lp = rp

        rp += 1


    return maxProfit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))
'''
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

'''
Buy LOW, sell HIGH

GIVEN:
    array of non-negative prices
STEPS:
    initialize left pointer equal to 0
    initialize right pointer equal to 1
    intialize maxProfit variable to keep track of the highest profit

    iterate through given array while right pointer is less than the length of array:
        if left pointer value is < than right pointer value:
            calculate current profit by subtracting value at left pointer by value at right pointer
            update the highest max profit, if the current profit is greater than what saved in the maxProfit variable

        else: left pointer is >= than right pointer:
            update the left pointer by setting it equal to the right pointer

        increment right pointer by 1

    return maxProfit


RESULT:

'''

