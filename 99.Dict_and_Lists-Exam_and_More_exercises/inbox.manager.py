emails_dict = {}
line = input()

while line != 'Statistics':
    args = line.split('->')
    command = args[0]
    username = args[1]
    if command == 'Add':
        if username not in emails_dict.keys():
            emails_dict[username] =[]
        else:
            print(f'{username} is already registered')
    elif command == 'Send':
        email = args[2]
        emails_dict[username].append(email)
    elif command == 'Delete':
        if username not in emails_dict.keys():
            print(f'{username} not found!')
        else:
            del emails_dict[username]

    line = input()
sorted_dict = dict(sorted(emails_dict.items(), key=lambda x: (-len(x[1]),x[0])))
print(f'Users count: {len(emails_dict.keys())}')
for key in sorted_dict.keys():
    print(f'{key}')
    for value in sorted_dict[key]:
        print(f' - {value}')
