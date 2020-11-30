line = input()

players_dict = {}
while line != 'Season end':
    if '->' in line:
        args = line.split(' -> ')
        player = args[0]
        position = args[1]
        skill = int(args[2])
        if player not in players_dict.keys():
            players_dict[player] = {position: skill}
            continue

        elif player in players_dict.keys() and position in players_dict[player] and skill > players_dict[player][position]:
            players_dict[player][position] = skill

        elif position not in players_dict[player]:
            players_dict[player].update({position: skill})

        new_dict = {k: sum(v.values()) for k, v in players_dict.items()}

    elif 'vs' in line:
        player_one, player_two = line.split(' vs ')

        if player_one in players_dict.keys() and player_two in players_dict.keys():
            player_one_total = new_dict[player_one]
            player_two_total = new_dict[player_two]
            is_won = False
            for key in players_dict[player_one].keys():
                for key2 in players_dict[player_two].keys():
                    if key == key2:
                        if player_one_total > player_two_total:
                            del players_dict[player_two]
                            del new_dict[player_two]
                            is_won = True
                            break
                        elif player_two_total > player_one_total:
                            del players_dict[player_one]
                            del new_dict[player_one]
                            is_won = True
                            break
                        else:
                            continue
                if is_won:
                    break

    line = input()

new_dict = dict(sorted(new_dict.items(),key = lambda x:x[1],reverse=True))
players_dict = dict(sorted(players_dict.items(),key = lambda x: (x[0], x[1].values())))

# for key,value in sorted(players_dict.items(),key= lambda x: (-sum(i for i in x[1].values()), x[0])):
#     if len(players_dict[key]) == 0:
#         continue
#     else:
#         print(f'{key}: {sum(value.values())} skill')
#
#     for key2, val in sorted(players_dict[key].items(), key=lambda x:(-x[1],x[0])):
#         print(f'- {key2} <::> {val}')
print(players_dict)