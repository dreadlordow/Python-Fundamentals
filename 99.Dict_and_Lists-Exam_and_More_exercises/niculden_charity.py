string = input()

line = input()
while True:
    if line == 'Finish':
        break
    args = line.split()
    command = args[0]
    if command == 'Replace':
        current_char = args[1]
        new_char = args[2]
        while current_char in string:
            string = string.replace(current_char, new_char)
        print(string)

    elif command == 'Cut':
        start_index = int(args[1])
        end_index = int(args[2])
        if (0 > start_index or start_index > len(string) or (0 > end_index or end_index > len(string))):
            print(f'Invalid indexes!')
            line = input()
            continue
        string = string[0:start_index] + string[end_index+1:]
        print(string)

    elif command == 'Make':
        criteria = args[1]
        if criteria == 'Upper':
            for char in string:
                string = string.replace(char, char.upper())
        elif criteria == 'Lower':
            for char in string:
                string = string.replace(char, char.lower())
        print(string)

    elif command == 'Check':
        str_to_check = args[1]
        if str_to_check in string:
            print(f'Message contains {str_to_check}')
        else :
            print(f"Message doesn't contain {str_to_check}")


    elif command == 'Sum':
        sum = 0
        start = int(args[1])
        end = int(args[2])
        substring = string[start:end+1]
        if (0 > start or start > len(string) or (0 > end or end > len(string))):
            print(f'Invalid indexes!')
            line = input()
            continue
        for char in substring:
            sum += ord(char)
        print(sum)

    line = input()
