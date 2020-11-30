def urgent_function(item,groceries_list):
    if item not in groceries_list:
        groceries_list.insert(0, item)
    return groceries_list


def unnecessary_function(item,groceries_list):
    if item in groceries_list:
        groceries_list.remove(item)
    else :
        pass
    return groceries_list


def correct_function(old_item, new_item, groceries_list):
    if old_item in groceries_list:
        for i, word in enumerate(groceries_list):
            if word == old_item:
                groceries_list[i] = new_item
    return groceries_list


def rearrange_function(item, groceries_list):
    if item in groceries_list:
        groceries_list.remove(item)
        groceries_list.append(item)
    return groceries_list


groceries_list = input().split('!')
input_line = input()

while  input_line != 'Go Shopping!':
    tokens = input_line.split()
    command = tokens[0]
    if command == 'Urgent':
        item = tokens[1]
        groceries_list = urgent_function(item, groceries_list)
    elif command == 'Unnecessary':
        item = tokens[1]
        groceries_list = unnecessary_function(item,groceries_list)
    elif command == 'Correct':
        old_item = tokens[1]
        new_item = tokens[2]
        groceries_list = correct_function(old_item, new_item, groceries_list)
    elif command == 'Rearrange':
        item = tokens[1]
        groceries_list = rearrange_function(item, groceries_list)


    input_line = input()

print(*groceries_list, sep=', ')