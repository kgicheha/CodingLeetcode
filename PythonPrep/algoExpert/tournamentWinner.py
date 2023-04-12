'''
Question Link:
https://www.algoexpert.io/questions/tournament-winner
'''
'''
GIVEN:
    1. array of pairs representing the teams tht have competed against each other
    2. array containing the results of each competition
STEPS:
    initialize a empty dictionary to keep track of scores

    traverse given competitions array:
        homeTeam will be the first element in each sub array
        awayTeam will be the second element in each sub array

        if the results of the game equals 1:
            this means that the hometeam won:
                so you need to increment the team score if it already exists in the scoreCount dictionary
                else:
                    add it to the score count with a score of 1
        else if the results of the game equals 0:
            this means the away team won
            so you need to increment the team score if it already exists in the scoreCount dictionary
                else:
                    add it to the score count with a score of 1


    return the key with the max value
RESULTS:
    return winner of the tournament
'''

def tournamentWinner(competitions, results):

    scoreCount = {}

    for currentGame in range(len(competitions)):
        homeTeam = competitions[currentGame][0]
        awayTeam = competitions[currentGame][1]
        print("HomeTeam",homeTeam)
        print("AwayTeam",awayTeam)


        if results[currentGame] == 1:
            if competitions[currentGame][0] not in scoreCount:
                scoreCount[competitions[currentGame][0]] = 1
            else:
                scoreCount[competitions[currentGame][0]] += 1
        elif results[currentGame] == 0:
            if competitions[currentGame][1] not in scoreCount:
                scoreCount[competitions[currentGame][1]] = 1
            else:
                scoreCount[competitions[currentGame][1]] += 1

    print(scoreCount)

    max_key = max(scoreCount, key= scoreCount.get)

    return max_key



competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]
results = [0,0,1]
print(tournamentWinner(competitions, results))
