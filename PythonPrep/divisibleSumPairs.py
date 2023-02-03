'''
Given an array of integers and a positive integer k,
determine the number of (i,j) pairs where i < j and ar[i] + ar[j]
is divisible by .
'''

'''
GIVEN:
    1. array of integers
    2. positive integer
    3. length of array
STEPS:
RESULT:
'''

def divisibleSumPairs(n, k, ar):
    pair_count = 0
    lp = 0

    for lp in range(n):

        rp = lp + 1

        while rp < n:
            if (lp < rp):
                if((ar[lp] + ar[rp]) % k == 0):
                    pair_count += 1
                    print(ar[lp],ar[rp])
            else:
                lp += 1
                rp = lp + 1
            rp += 1
    print(pair_count)

divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2])