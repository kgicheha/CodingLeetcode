def migratoryBirds(arr):

    countTracker = {}

    for i in range(len(arr)):
        if arr[i] in countTracker:
            countTracker[arr[i]] += 1

        else:
            countTracker[arr[i]] = 1

    maxValue = float("inf")
    highestCount = float("-inf")

    for i in countTracker:
        if countTracker[i] > highestCount:
            maxValue = i
            highestCount = countTracker[i]

        elif countTracker[i] == highestCount:
	        maxValue = min(i, maxValue)


    return  maxValue

arr = [1,1,2,2,3]
# 1
print(migratoryBirds(arr))

'''
GIVEN:
    array of integers
STEPS:
    if len(arr) == 0:
        return 0

    # BRUTE FORCE:
    create a hashmap to store the count of the values

    iterate through given array:
        if value is in hashmap:
            increment its value by 1
        else:
            add value to hashmap with value 1


    maxValue = float("-inf")
    highestCount = float("-inf")


    iterate though hashmap:
        if value of i is > than the highestCount:
            set maxValue to i and highestCount to current value

        elif value of i == highestCount:
            set maxValue to min(i, maxValue)

    return maxValue

arr = [1,1,2,2,3]
{1:2,
2:2,
3:1
}

'''