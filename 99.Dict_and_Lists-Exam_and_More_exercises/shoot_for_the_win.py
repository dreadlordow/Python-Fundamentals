sequence = list(map(int, input().split()))

input_command = input()
res = []
target_to_subtract = 0
shot_targets = 0
while not input_command == 'End':
    counter = 0
    current_target = int(input_command)
    if current_target > len(sequence):
        input_command = input()
        continue
    if 0 <= current_target < len(sequence) and sequence[current_target] != -1:
        target_to_subtract = sequence[current_target]
        sequence[current_target] = -1
        shot_targets += 1
        for target in sequence :
            if target_to_subtract < target and sequence[counter] != -1:
                sequence[counter] -= target_to_subtract
            elif target_to_subtract >= target and sequence[counter] != -1:
                sequence[counter] += target_to_subtract

            counter += 1







    input_command = input()
print(f"Shot targets: {shot_targets}", end=' -> ')
print(*sequence, sep= ' ')
