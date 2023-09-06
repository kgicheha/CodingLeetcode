'''
Question Link:
https://www.algoexpert.io/questions/tandem-bicycle
'''
'''

GIVEN:
    2 lists of positive integers
STEPS:
    sort the given array in ascending order
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
