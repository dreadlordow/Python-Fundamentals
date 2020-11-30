neighbourhood = list(map(int, input().split('@')))

starting_index = 0
while True:
    delivery = input()
    if delivery == 'Love!':
        break
    tokens = delivery.split()
    index_to_jump = int(tokens[1])
    starting_index += index_to_jump

    if starting_index >= len(neighbourhood):
        starting_index = 0
    if neighbourhood[starting_index] == 0 :
        print(f"Place {starting_index} already had Valentine's day.")
    else:
        neighbourhood[starting_index] -= 2
        if neighbourhood[starting_index] == 0 :
            print(f"Place {starting_index} has Valentine's day.")

    last_index = starting_index

print(f"Cupid's last position was {last_index}.")

res = [x for x in neighbourhood if x != 0]
if len(res) > 0 :
    print(f"Cupid has failed {len(res)} places.")
else :
    print(f'Mission was successful.')