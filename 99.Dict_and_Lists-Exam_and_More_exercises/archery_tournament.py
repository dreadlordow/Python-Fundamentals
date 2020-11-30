def add_stop(args, line, string):
    index = int(args[1])
    string_to_add = args[2]
    if 0 < index < len(string):
        string = string[:index] + string_to_add + string[index:]
    return string


def remove_stop(args, line, string):
    start_index = int(args[1])
    end_index = int(args[2])
    if 0 <start_index < len(string) and 0 < end_index < len(string):
        string = string[:start_index] + string[end_index+1:]
    return string


def switch_strings(args, line, string):
    old_string = args[1]
    new_string = args[2]
    if old_string in string:
        string = string.replace(old_string,new_string)
    return string

string = input()
line = input()

while line != 'Travel':
    args = line.split(':')
    command = args[0]

    if command == 'Add Stop':
        string = add_stop(args, line, string)
        print(string)
    elif command == 'Remove Stop':
        string = remove_stop(args, line, string)
        print(string)
    elif command == 'Switch':
        string = switch_strings(args, line, string)
        print(string)



    line = input()
print(f'Ready for world tour! Planned stops: {string}')