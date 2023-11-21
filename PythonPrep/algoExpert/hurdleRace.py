def hurdleRace(k, height):
    maxNumber = max(height)

    if maxNumber > k:
        return maxNumber - k
    else:
        return 0


k = 4
height = [1,6,3,5,2]
print(hurdleRace(k, height))

'''
GIVEN:

STEPS:
    get the max number in the given height array

    return max number - k if maxnumber > k else return 0
RESULTS:
    the minimum number of doses required
        always >= 0
'''