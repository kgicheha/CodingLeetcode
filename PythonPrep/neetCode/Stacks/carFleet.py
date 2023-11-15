def carFleet(target, position, speed):
    pair = []

    for i in range(len(position)):
        pair.append([position[i], speed[i]])

    stack = []

    for position, speed in sorted(pair)[::-1]:
        timeToReachTarget = (target - position) / speed
        stack.append(timeToReachTarget)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()


    return len(stack)
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(carFleet(target, position, speed))

'''
Link: https://leetcode.com/problems/car-fleet/
'''
'''
GIVEN:
    target,
    array of positions,
    array of speed

STEPS:
    initialize pair array list --> will be used to store the pair of position and speed at each position

    iterate through given position array list:
        at each index: append the position and speed to the pair array list

    initialize stack equal to empty array list

    sort the pair array list

    iterate though pair list in reverse order:

        calculate the time it will take to reach the target
            formula = (target - position) / speed
            append the value to the stack


        if the stack has 2 or more or elements AND the value of the 2nd to last element is more or equal to the last element:
                this means that the 2nd last car will get there faster than the last car
                so we need to combine them as 1 car fleet
            pop out the second last element from the stack

    return the length of the stack



RESULTS:
'''