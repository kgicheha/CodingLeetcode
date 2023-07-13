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
    print("yes")