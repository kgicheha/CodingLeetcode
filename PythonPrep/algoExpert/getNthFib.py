'''
Question Link:
https://www.algoexpert.io/questions/nth-fibonacci
'''

def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)

n = 9
print(getNthFib(n))