'''
The SuperBowl Lottery is about to commence, and there are several lottery tickets being sold,
and each ticket is identified with a ticket ID.
In one of the many winning scenarios in the Superbowl lottery,
a winning pair of tickets is:

Concatenation of the two ticket IDs in the pair, in any order,
contains each digit from 0 to 9 at least once.


Your task is to find the number of winning pairs of distinct tickets,
such that concatenation of their ticket IDs (in any order)
makes for a winning scenario.
Complete the function winningLotteryTicket which takes a string array
of ticket IDs as input,
and return the number of winning pairs.
'''
'''
GIVEN: inputs
STEPS:
    variable that keeps count of the pairs

RESULT:
    print the total number of pairs that when combined, they have all the numbers from 0-9

'''
def winningLotteryTicket(tickets):
    winning_pair_count = 0
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lp = 0
    rp = 1

    while(rp < len(tickets)) and (lp < len(tickets) - 1):
        ticket_comb = tickets[lp] + tickets[rp]


        if set(ticket_comb) == set(nums):
            winning_pair_count += 1
        rp += 1

        if(rp == len(tickets)):
            lp += 1
            rp = lp + 1

    return winning_pair_count


tickets = ['129300455', '5559948277', '012334556', '56789', '123456879']

print(winningLotteryTicket(tickets))