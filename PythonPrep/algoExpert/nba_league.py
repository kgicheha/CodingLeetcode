'''
league has 12 players
15 total rounds

total picks = players * total rounds

for number in the range of 0 to total picks:
    if number is divisble by the number of players:
        get the range from
'''
# if round is ODD: 4th pick in round
# if round if EVEN: 9th pick in round


def determine_draft_picks(rounds, total_players):
    picks = []
    current_round = 0

    for round in range(1, rounds + 1):
        if round % 2 == 1:
            # Odd-numbered round (4th pick)
            pick_number = 3 + (round - 1) * total_players
        else:
            # Even-numbered round (9th pick)
            pick_number = 10 + (round - 1) * total_players

        current_round += 1
        print("Current Round", current_round)
        print("Pick:", pick_number)

        picks.append(pick_number)

    return picks

rounds = 15
total_players = 12
your_picks = determine_draft_picks(rounds, total_players)
print(your_picks)