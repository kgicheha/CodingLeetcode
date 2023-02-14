'''
Given an array of integers, sort
the array in ascending order using the Bubble Sort algorithm above
'''
'''
GIVEN:
    array
STEPS:
    loop through given array
        if current number > that [current number + 1]:
            swap them
        else:
            move on to the next number
RESULT:
    sorted array in ascending order
'''
def countSwaps(a):

    swapCount = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if (a[j] > a[j+1]):
                swapCount += 1
                a[j], a[j+1] = a[j+1], a[j]

    print("Array is sorted in", swapCount, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a.pop())

# a[-1]
countSwaps([6,4,1])