'''
Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests.
Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory.
Each contest is described by two integers, L[i] and T[i] :

L[i] is the amount of luck associated with a contest.
If Lena wins the contest, her luck balance will decrease by L[i]; if she loses it, her luck balance will increase by

 T[i] denotes the contest's importance rating.
 It's equal to 1 if the contest is important, and it's equal to 2 if it's unimportant.

 If Lena loses no more than K important contests,
 what is the maximum amount of luck she can have after competing in all the preliminary contests?
 This value may be negative.
'''


'''
GIVEN:
    1. number of important loses Lena can lose, represented as K
    2. 2D array of integers where each
STEPS:
    create luck balance variable and initialize it to 0
    sort the given 2d based on the 1st element in each array

    loop while k <= 0:
        if x[1] == 0:
            add x[0] to the balance
        elif x[1] == 1:
            addx[0] to the balance
            decrement k by 1

RESULT:
    return maximum luck balance achievable
'''

def luckBalance(k, contests):

    balance = 0
    important_contests = k
    print(contests)

    sorted_arr = sorted(contests, key = lambda x:x[0], reverse=True)
    print(sorted_arr)

    for row in contests:
        for elem in row:
            if elem == 0:
                print(row, elem)
                balance += row
                # balance = balance + row


    print(balance)




contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
k = 3
luckBalance(k, contests)