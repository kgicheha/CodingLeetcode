'''
An arcade game player wants to climb to the top of the leaderboard
and track their ranking.
The game uses Dense Ranking, so its leaderboard works like this:

    The player with the highest score is ranked number 1 on the leaderboard.
    Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

'''

'''
Example
ranked = [100,90,90,80]
player = [70,80,105]
'''

'''
GIVEN: two arrays: ranked and player scores
STEPS:
    create a SET of ranked scores
        This elimates duplicates from given ranked score array
    sort the SET of the ranked scores
        in reverse order

    iterate player score array
        if the score is greater than the first number in the ranked score
            add a 1 to the results array
                Meaning the player is in first place
        else if the score is less than the last number in the ranked score
            add [the length of SET of ranked scores + 1] to the results array
RETURN: rank of player scores rank in an array
'''


def climbingLeaderboard(ranked, player):



    # Sol3
   result = []
   unique_scores = sorted(set(ranked), reverse=True)
   print(unique_scores)

   for score in range(len(player)):
    if(score >= unique_scores[0]):
        result.push(1)
    elif (score < unique_scores[len(unique_scores) - 1]):
        result.push(len(unique_scores) +1)


    print(result)
ranked = [100,90,90,80]
player = [70,80,105]

climbingLeaderboard(ranked, player)