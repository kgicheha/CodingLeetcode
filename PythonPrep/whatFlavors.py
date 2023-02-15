'''
Each time Sunny and Johnny take a trip to the Ice Cream Parlor,
they pool their money to buy ice cream. On any given day,
the parlor offers a line of flavors.
Each flavor has a cost associated with it.

Given the value of money  and the cost of each flavor for t trips
to the Ice Cream Parlor, help Sunny and Johnny choose two distinct
flavors such that they spend their entire pool of money during each visit.
ID numbers are the 1- based index number associated with a cost.
For each trip to the parlor, print the ID numbers for the two types of
ice cream that Sunny and Johnny purchase as two space-separated integers
on a new line. You must print the smaller ID first and the larger ID second.


Two ice creams having unique IDs i and j may have the same cost (i.e., cost[i] == cost[j] ).
'''

'''
GIVEN:
    array of integers
    money
STEPS:
    initilze empty object that will be used to store the difference between the current number and the given money

    loop through the given arry and store the absolute diffnerce between the current number and money to the array

RESULT
'''

def whatFlavors(cost, money):
    diff ={}
    semi_result =[]
    result = []

    for i in range(len(cost)):
        cur_dif = (money - cost[i])

        if cur_dif > 1:
            diff[cost[i]] = cur_dif

    print(diff)

    for key in diff:
        if diff[key] in cost:
            semi_result.append(diff[key])

    for i in range(len(semi_result)):
        for j in range(len(cost)):
            if semi_result[i] == cost[j]:
                result.append(j+1)

    print(semi_result)
    print(result)
cost = [2,1,3,5,6]
money = 5
whatFlavors(cost, money)