'''
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

'''
'''
Example 1:

input: n = 3
output =  3
explanation:
    There are three distict combination in which you can climb to the top
    1. 1 step + 1 step + 1 steps
    2. 1 step + 2 steps
    3. 2 steps + 1 step
'''
'''
GIVEN: total number of steps
STEPS:
    #BOTTOM UP Dynamic programming approach
        Similar to the fibonacci sequence where the current value is the sum of the previous two values


    Base Case:
        the last two values will be equal to 1 because you can only take 1 option to get to the destination
        create and set two pointers both equal to 1
    iterate array from the beginning to n-1 positon
        this will stop at the 3rd last position because the last two values are always determined to be 1

        as you iterate
            create a temp variable and set it equal to the first pointer
                This way the value of the first pointer is stored somewhere before we change its value
            set the first pointer equal to the sum of itself and the second pointer
            set the 2nd pointer equal to the temp variable
                aka set the pointer equal to what the first pointer was previously equal to

        return first pointer
RETURN: the number of distinct ways in which you can climb to the top
'''

def climbStairs(n):

    pointer_one, pointer_two = 1,1

    for i in range(n-1):
        temp = pointer_one
        pointer_one = pointer_one + pointer_two
        pointer_two = temp
    return pointer_one

print(climbStairs(5))