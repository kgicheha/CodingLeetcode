def staircaseTraversal(height, maxSteps):

    memoize = {0:1, 1:1}
    return numberofWaysToTop(height, maxSteps, memoize)

def numberofWaysToTop(height, maxSteps, memoize):

    if height in memoize:
        return memoize[height]

    numberOfWays = 0

    for step in range(1, min(maxSteps,height) + 1):
        numberOfWays += numberofWaysToTop(height - step, maxSteps, memoize)

    memoize[height] = numberOfWays

    return numberOfWays

height = 4
maxSteps = 2

print(staircaseTraversal(height, maxSteps))


'''
GIVEN:
    two positive integers:
        - height (the number of steps in the staircase)
        - maximum number of steps you can advance up the staircase at a time

STEPS:
RESULT:
    return the number ofway in which you can climb the staircase

'''

'''
Example:

    height = 3
    maxSteps = 2

    result = 3

        can climb :
            1 step, 1 step, then 1 step
            1 step, then 2 steps
            2, steps then 1 steps
'''