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
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    minSpeed = 0
    maxSpeed = 0

    for idx in len(redShirtSpeeds):
        if fastest = 'true':
            current_redShirt = redShirtSpeeds[-1]
            current_redShirt

    return redShirtSpeeds


redShirtSpeeds = [5,5,3,9,2]
blueShirtSpeeds = [3,6,7,2,1]
fastest = True

print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest))
