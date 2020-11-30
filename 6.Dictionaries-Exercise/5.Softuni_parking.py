n = int(input())

my_dict = {}

for _ in range(n):
    line = input().split()
    command = line[0]
    username = line[1]

    if command == 'register':
        plate = line[2]
        if username in my_dict:
            print(f'ERROR: already registered with plate number {plate}')
        else :
            my_dict[username] = plate
            print(f'{username} registered {plate} successfully')


    elif command == 'unregister':
        if username in my_dict:
            my_dict = {k:v for k,v in my_dict.items() if k != username}
            print(f'{username} unregistered successfully')
        else :
            print(f'ERROR: user {username} not found')

for k,v in my_dict.items():
    print(f'{k} => {v}')
