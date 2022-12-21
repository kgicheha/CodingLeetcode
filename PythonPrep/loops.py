'''
Print the square of each number on a separate line.
'''

'''
GIVEN: number

STEPS
    while loop from 0 to given number
    multiply each number by itself

RESULT: print the sqaure of each number
'''

def division(n):
    i = 0
    while(i < n):
        print(i * i)
        i+=1


division(5)
