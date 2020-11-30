team_a = [1] * 11
team_b = [1] * 11

cards_input = input().split()
# tokens = cards_input.split('-')
team_a_players = 11
team_b_players = 11

terminated = False

for tokens in cards_input:
    cards = tokens.split('-')
    card = cards[0]
    number = int(cards[1]) - 1
    if card == 'A':
        if not team_a[number] == 0:
            team_a[number] -= 1
            team_a_players -=1
        if team_a_players < 7 :
            terminated = True
            break
    elif card == 'B':
        if not team_b[number] == 0:
            team_b[number] -= 1
            team_b_players -= 1
        if team_b_players < 7 :
            terminated = True
            break
print(f'Team A - {team_a_players}; Team B - {team_b_players}')
if terminated:
    print(f'Game was terminated')