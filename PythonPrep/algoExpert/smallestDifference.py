def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    lowest_difference = float("inf")
    current_difference = float("inf")
    result = []

    pointer1 = 0
    pointer2 = 0

    while pointer1 < len(arrayOne) and pointer2 < len(arrayTwo):
        firstNum = arrayOne[pointer1]
        secondNum = arrayTwo[pointer2]

        if firstNum < secondNum:
            current_difference = secondNum - firstNum
            pointer1 += 1
        elif firstNum > secondNum:
            current_difference = firstNum - secondNum
            pointer2 += 1
        else:
            return [firstNum, secondNum]

        if lowest_difference > current_difference:
            lowest_difference = current_difference
            result = [firstNum, secondNum]
    return result



arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

print(smallestDifference(arrayOne, arrayTwo))

# sortedArray1: [-1, 3, 5, 10, 20, 28]
# sortedArray2: [15, 17, 26, 134, 135]


   # for i in arrayOne:
    #     for j in arrayTwo:
    #         current_difference = abs(i - j)
    #         if current_difference < lowest_difference:
    #             lowest_difference = current_difference
    #             result = []
    #             result.append(i)
    #             result.append(j)

    # return result