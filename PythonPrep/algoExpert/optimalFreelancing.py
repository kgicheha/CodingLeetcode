'''
Question Link:
https://www.algoexpert.io/questions/optimal-freelancing
'''

'''
GIVEN:
    an array of objects
        each object has a deadline and payment

STEPS:
    initialize maxProfit equal to 1

    initialize currentDay equal to 1

    while currentDay <= 7:
        if "deadline" == curentDay:
            increment maxProfit by the max payment for that day

        currentDay += 1

    return maxProfit

RESULT:
    return a max profit that can be obtained in a 7-day period

'''


def optimalFreelancing(jobs):

    maxProfit = 0

    currentDay = 1

    currentDayPmt = []

    while currentDay <= 7:

        for job in jobs:
            if job['deadline'] == currentDay:
                currentDayPmt.append(job['payment'])

                maxProfit += max(currentDayPmt)
        # currentDayPmt = []
            currentDay += 1

    print(currentDayPmt)
    print(maxProfit)
jobs =[
    {"deadline": 1, "payment":1},
    {"deadline": 2, "payment":1},
    {"deadline": 2, "payment":2},

]

optimalFreelancing(jobs)