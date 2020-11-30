sequence = list(input().split())

move_counter = 0

integer_input = input()
while True:
    index_token = integer_input.split(' ')
    if len(index_token) > 1:
        first_index = int(index_token[0])
        second_index = int(index_token[1])
    else :
        integer_input = input()

    move_counter += 1
    middle_sequence = len(sequence) // 2

    if first_index == second_index or (first_index > len(sequence) or second_index > len(sequence)
                                       or (first_index < 0 or second_index < 0)):
        print(f'Invalid input! Adding additional elements to the board')
        thing_to_insert = str(-move_counter) + 'a'
        sequence.insert(middle_sequence, thing_to_insert)
        sequence.insert(middle_sequence, thing_to_insert)

    elif sequence[first_index] == sequence[second_index]:
        print(f'Congrats! You have found matching elements - {sequence[first_index]}!')
        indices = {first_index, second_index}
        new_list = [v for i, v in enumerate(sequence) if i not in indices]
        sequence = new_list

    elif sequence[first_index] != sequence[second_index]:
        print(f'Try again!')

    if len(sequence) == 0:
        print(f"You have won in {move_counter} turns!")
        break

    if len(sequence) == 1:
        break

    integer_input = input()
    if integer_input == 'end':
        break

if len(sequence) >= 1:
    print(f"Sorry you lose :(")
    print(*sequence, sep=' ')
