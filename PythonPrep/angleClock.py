'''
1344. Angle Between Hands of a Clock

Given two numbers, hour and minutes,
return the smaller angle (in degrees)
formed between the hour and the minute hand.
'''

'''
EXAMPLE
Input: hour = 12, minutes = 30
Output: 165
'''

'''
STEPS:
    Full circle = 360 degrees
    Calculate degree per hour
        full circle has 12 hours
        degree_per_hour = full circle / 12 hours
        degree_per_hour = 360 / 12
        degree_per_hour = 30

    Calculate degree per minute
        full circle has 60 minutes
        degree_per_minute = full circle / 60
        degree_per_minute = 360 / 60
        degree_per_minute = 6

    Calculate total degree of given hour hand
        degree_given_hour = (hour + (minute/60)) * degree_per_hour

    Calculate total degree of given minute hand
        degree_given_minutes = minutes * degree_per_minute


    Calculate angle
        absolute value of (degree_given_hour - degree_given_minutes)

    if angle is more than 180 degrees
        set the angle equal to the smaller value
        angle = 360 degrees - angle

    return angle


TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
'''


def angle_clock(hour, minutes):

    degree_per_hour = 360 / 12
    degree_per_minute = 360 / 60

    degree_of_given_hour = ((hour % 12) + (minutes/60)) * degree_per_hour
    degree__of_given_minutes = minutes * degree_per_minute

    angle = abs(degree_of_given_hour - degree__of_given_minutes)

    if (angle > 180):
        angle = 360 - angle

    print(angle)


angle_clock(12, 30)
