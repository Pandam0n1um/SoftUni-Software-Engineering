players_dict = {}

while True:
    command = input()
    if command == "Season end":
        break

    if "vs" in command:
        common_pos = []
        player1, player2 = command.split(" vs ")
        if player1 in players_dict and player2 in players_dict:
            common_pos = [x for x in players_dict[player1] if x in players_dict[player2]]
        if common_pos:
            if sum(players_dict[player1].values()) > sum(players_dict[player2].values()):
                del players_dict[player2]
            elif sum(players_dict[player2].values()) > sum(players_dict[player1].values()):
                del players_dict[player1]
    else:
        player1, position, skill = command.split(" -> ")
        skill = int(skill)
        if player1 not in players_dict:
            players_dict[player1] = {}

        if position in players_dict[player1]:
            curr_value = players_dict[player1][position]
            players_dict[player1][position] = max(curr_value, skill)
        else:
            players_dict[player1][position] = skill
playerskill_sorted=(sorted(players_dict.items(), key=lambda x: (-sum(x[1].values()),x[0])))
print(playerskill_sorted)
for player,rank in playerskill_sorted:
    print(f'{player}: {sum(rank.values())} skill')
    rank_sorted=sorted(rank.items(),key=lambda x: (-x[1],x[0]))
    for position,skill in rank_sorted:
        print(f"- {position} <::> {skill}")


# print(playerskill_sorted)
