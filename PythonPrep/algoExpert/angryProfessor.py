def angryProfessor(k,a):
    onTimeCounter = 0

    for i in range(len(a)):
        if a[i] <= 0:
            onTimeCounter += 1

    print(onTimeCounter)
    if onTimeCounter < k:
        return "YES"

    else:
        return "NO"


k = 2
# a = [0,-2,-1,1,2]
a = [-1,-3,4,2]
a = [0,-1,2,1]
print(angryProfessor(k,a))
'''
GIVEN:
    threshold
    array of integers based on their arrival time
        negative and 0 integers means they arrived on or before deadline
        positive means they arrived late
STEPS:

    initialize variable that keeps track of count of student who are on time

    iterate through given array:
        if current number is <=0:
            increment the counter by one

    if counter < threshold:
        return "YES"
    else:
        return "NO"
RESULT:
    Return "YES" if the numbers of students that are last > the threshold
    else return "NO"

'''