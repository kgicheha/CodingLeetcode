'''
Link:
https://www.algoexpert.io/questions/tournament-winner

'''
'''
GIVEN:
    an array of pairs representing the teams that competed against each other
        competitions = [homeTeam, awayTeam]
            represented as strings
    an array containing the results of each competition
        0 means the awayTeam won
        1 means the homeTeam won

STEPS:
    create empty dictionary that tracks the score

    loop through given competitions array
        in the current competition:
            if the result is 0:
                if the awayTeam is in the score dictionary:
                    increments its score by 1
                else:
                    add the awayTeam in the scores dictionary by setting the score to 1
            if the result is 1:
                if the home team is already present in the score dictinary:
                    increment their score by 1
                else:
                    add the homeTeam in the scores dictionary by setting the score to 1


    return the team with the highest max number in the dicitionary

RESULT:
    returns the winner of the tournament
'''

'''
EXAMPLE:

'''


def tournWinner(competitions, results):

    scores = {}

    curResult = 0
    for competition in competitions:
        if results[curResult] == 0:
            if competition[1] in scores:
                scores[competition[1]] += 3
            else:
                scores[competition[1]] = 3
        else:
            if competition[0] in scores:
                scores[competition[0]] += 3
            else:
                scores[competition[0]] = 3

        curResult += 1

    highestScore = max(scores.values())

    for key, value in scores.items():
        if value == highestScore:
            print(key)


competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]
results = [0,0,1]
tournWinner(competitions, results)