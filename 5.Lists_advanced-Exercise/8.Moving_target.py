def shoot_command(sequence, index, power):
    sequence[index] -= power
    if sequence[index] <= 0:
        del sequence[index]
    return sequence


def add_command(sequence, index, value):
    sequence.insert(index, value)
    return sequence


def strike_command(sequence, index, radius):
    del sequence[index]
    del sequence[index: index + radius]
    del sequence[index - radius: index]
    return sequence


sequence = list(map(int, input().split()))
input_command = input()

while not input_command == 'End':
    tokens = input_command.split()
    command = tokens[0]
    index = int(tokens[1])
    if command == 'Shoot':
        power = int(tokens[2])
        if 0 <= index < len(sequence):
            sequence = shoot_command(sequence, index, power)

    elif command == 'Add':
        value = int(tokens[2])
        if 0 <= index < len(sequence):
            sequence = add_command(sequence, index, value)
        else:
            print(f'Invalid placement!')

    elif command == 'Strike':
        radius = int(tokens[2])
        start = index - radius
        end = index + radius

        if start >= 0 and end < len(sequence):
            del sequence[start: end + 1]

        else:
            print(f'Strike missed!')

    input_command = input()

print(*sequence, sep='|')