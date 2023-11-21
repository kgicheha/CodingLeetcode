def breakingRecords(scores):

    lowestScore = scores[0]
    lowestScoreRecordBreakCount = 0


    highestScore = scores[0]
    highestRecordBreakCount = 0

    for i in range(1,len(scores)):
        if scores[i] < lowestScore:
            lowestScoreRecordBreakCount += 1
            lowestScore = scores[i]

        if scores[i] > highestScore:
            highestRecordBreakCount += 1
            highestScore = max(highestScore, scores[i])


    return [highestRecordBreakCount, lowestScoreRecordBreakCount]

# scores = [3, 4, 21, 36, 10, 28, 35, 5,24, 42]
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
print(breakingRecords(scores))
# 4 0

'''
GIVEN:
    array of scores
STEPS:
    initialize lowestScore index  equal to 0

    initialize highestScore equal to the score[0]
    initialize recordBreakCount equal to 0

    iterate through given array from index 1 to end of array:
        if the current number is lower than the score at the lowestScore Index:
            set the lowest current index to the current index

        if current number is > the highest Score:
            increment record break count by one
            set highest score to the current number


    return [recordBreakCount, lowestScoreIndex]

RESULT:
    the number of times Maria breaks her records
    the least points scored
'''