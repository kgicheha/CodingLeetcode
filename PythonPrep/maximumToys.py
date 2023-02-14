'''
Mark and Jane are very happy after having their first child.
Their son loves toys, so Mark wants to buy some.
There are a number of different toys lying in front of him,
tagged with their prices. Mark has only a certain amount to spend,
and he wants to maximize the number of toys he buys with this money.
Given a list of toy prices and an amount to spend,
determine the maximum number of gifts he can buy.

Note:
    Each toy can by purchased only once
'''

'''
GIVEN:
    array of integers
    k budget
STEPS:
    variable that keeps track of the sum
    variable that keep track of count

    loop though given array
        if the current Sum + current number is < k:
            increment count by 1
        elif current Sum + current number is > k:
            go to the next number
RESULT:
    return the maximum number of gifts Mark can buy with a budget of k
'''

def maximumToys(prices, k):
    prices.sort()

    sum = 0
    count = 0

    for i in range(len(prices)):
        sum = sum + prices[i]
        print(sum)

        if sum < k:
            count += 1

    print(count)

prices =[1,2,3,4]
prices =[1,12,5,111, 200, 1000, 10]
k = 50
maximumToys(prices, k)