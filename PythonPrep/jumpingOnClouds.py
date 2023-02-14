'''
There is a new mobile game that starts with consecutively numbered
 clouds.
 Some of the clouds are thunderheads and others are cumulus.
 The player can jump on any cumulus cloud having a number that
 is equal to the number of the current cloud plus 1 or 2 .
 The player must avoid the thunderheads.
 Determine the minimum number of jumps it will take to
 jump from the starting postion to the last cloud.
 It is always possible to win the game.

For each game, you will get an array of clouds numbered
if they are safe or  if they must be avoided.
'''

'''
GIVEN: array with 0s and 1s
    0 digits are safe, 1 digit are not safe
STEPS:
    intialize a count that keeps track of the amount of steps from the starting point to the finish

RESULT:
    the minimum number of jumps it will take to jump from the starting cloud to the last cloud
'''
def jumpingOnClouds(c):
    minTravel = 0
    i = 0

    while i < len(c)-1:
        if i < len(c) - 2 and c[i + 2] == 0 :
            i += 2
        else:
            i += 1
        minTravel += 1

    print(minTravel)



c= [0,0,0,1,0,0]
# c = [0,1,0,0,0,1,0]
jumpingOnClouds(c)
