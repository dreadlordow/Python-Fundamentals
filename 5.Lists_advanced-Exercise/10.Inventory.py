starting_items = list(input().split(', '))

command_input = input()

while command_input != 'Craft!' :
    tokens = command_input.split(' - ')
    command = tokens[0]
    if command == 'Collect':
        item = tokens[1]
        if item in starting_items:
            command_input = input()
            continue
        starting_items.append(item)
    elif command == 'Drop':
        item = tokens[1]
        if item in starting_items:
            starting_items.remove(item)
    elif command == 'Combine Items':
        split = tokens[1].split(':')
        old_item = split[0]
        new_item = split[1]
        if old_item in starting_items:
            index = starting_items.index(old_item)
            new_index = index + 1
            starting_items.insert(new_index, new_item)
    elif command == 'Renew':
        item = tokens[1]
        if item in starting_items:
            starting_items.remove(item)
            starting_items.append(item)


    command_input = input()

print(*starting_items, sep=', ')