'''
Question Link:
https://www.algoexpert.io/questions/tandem-bicycle
'''
'''

GIVEN:
    2 lists of positive integers
STEPS:
    if the given fastest input is 'True':
        sort the given redShirtSpeeds list in descending order to pair the largest numbers in that list, with the smallest number in the BlueShirtSpeed list
            this will help to get the max number
    else:
        sort the given resShirtSpeeds in ascending order get the min value while pairing with the blueShirtSpeeds list
    sort the given array in ascending order

    sort the given blueShirtSpeeds in ascending order

    initialize a result variable to 0

    iterate through given lists and pair each number from one list with the number other list
    store the max value between the two pair to the results variable

    return the result

RESULT:
    if fastest = true,
        return the maximum possible total speed
    else:
        return the minimum total speed
'''
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    if fastest == 'True':
        redShirtSpeeds.sort(reverse=True)
    else:
        redShirtSpeeds.sort()

    blueShirtSpeeds.sort()

    result = 0

    for i in range(len(redShirtSpeeds)):
        result += max(redShirtSpeeds[i],blueShirtSpeeds[i])

    return result


redShirtSpeeds = [5,5,3,9,2]
blueShirtSpeeds = [3,6,7,2,1]
fastest = True

print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest))
