'''
Given an integer, n , print its first 10 multiples.
Each multiple n * i (where 1 <=i <=10)
should be printed on a new line in the form: n x i = result.

'''

def loop(N):
 i = 1
 while(i <= 10):
    result = N * i
    print(N, "x",i,"=",result)
    i += 1


loop(3)