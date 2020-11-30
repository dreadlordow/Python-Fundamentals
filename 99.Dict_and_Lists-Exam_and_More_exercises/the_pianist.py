n = int(input())
my_dict = {}
for _ in range(n):
    piece, composer, key = input().split('|')
    if piece not in my_dict:
        my_dict[piece] = [composer, key]

while True:
    inpt = input()
    if inpt == 'Stop':
        break
    line = inpt.split('|')
    command = line[0]
    piece = line[1]
    if command == 'Add':
        composer = line[2]
        key = line[3]
        if piece in my_dict:
            print(f'{piece} is already in the collection!')
        else:
            my_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command == 'Remove':
        if piece in my_dict.keys():
            del my_dict[piece]
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    elif command == 'ChangeKey':
        new_key = line[2]
        if piece in my_dict.keys():
            my_dict[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')


sorted_dict = dict(sorted(my_dict.items(), key=lambda x:(x[0],x[1][0])))

for piece in sorted_dict.keys():
        print(f"{piece} -> Composer: {sorted_dict[piece][0]}, Key: {sorted_dict[piece][1]}")