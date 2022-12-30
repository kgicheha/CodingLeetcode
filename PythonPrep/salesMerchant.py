'''
There is a large pile of socks that must be paired by color.
Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.
'''

'''
EXAMPLE 1:
n = 7
ar = [1,2,1,2,1,3,2]
There is one pair of color 1 and one of color 2 .
There are three odd socks left,
one of each color. The number of pairs is 2
'''

'''
GIVEN: arr, and n
STEPS:
    create empty object for frequecy count
    iterate given array
        for i in range of array:
            add each item to the empty object

        define counter
        get the values from the empty object
            if value is more that 1:
                increase count by 1

RETURN: the number of pairs

'''
def sockMerchant(ar):
    sock_pair ={}
    pairs =0

    for i in range(len(ar)):
        sock = ar[i]
        if(sock in sock_pair):
            sock_pair[sock] +=1
        else:
            sock_pair[sock] = 1

    for sock in sock_pair:
        pairs += sock_pair[sock] //2


    print(sock_pair)
    print(pairs)



sockMerchant([1,2,3,4,4,1])