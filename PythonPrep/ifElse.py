
"""
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20 , print Not Weird"


print "Weird"
    1. odd,
    2. even and in the range of 6 and 20

print "Not Weird"
    1. even and in the range of 2 to 5
    2. even and greater that 20

"""

"""
GIVEN: number
STEPS:

    if n % 2 === 0:
        if (n > )


RETURN: print "Weird" or "Weird"
"""

def my_function(n):

    #BRUTE FORCE
    if (n % 2 == 0):
        if (n >= 2) or (n <= 5) or (n > 20):
            print('Not Weird')
        else:
            print("Weird")
    else:
        print("Weird")