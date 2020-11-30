wagons = int(input())
wagon_list = [0] * wagons




while True:
    tokens = input().split()
    command = tokens[0]
    if command == 'End':
        break


    if command == 'add':
        people_to_add = int(tokens[1])
        wagon_list[-1] += people_to_add

    elif command == 'insert':
        index = int(tokens[1])
        people_to_insert = int(tokens[2])
        wagon_list[index] += people_to_insert

    elif command == 'leave':
        index = int(tokens[1])
        people_to_leave = int(tokens[2])
        wagon_list[index] -= people_to_leave



print(wagon_list)