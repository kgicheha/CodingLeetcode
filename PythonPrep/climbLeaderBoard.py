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

def climbingLeaderboard(ranked, player):