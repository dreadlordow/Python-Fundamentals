my_dict = {}

line = input()
unliked_meals = 0
while line != 'Stop':
    command, guest, meal = line.split('-')
    if command == 'Like':
        if guest not in my_dict:
            my_dict[guest] = []
        if meal not in my_dict[guest]:
            my_dict[guest].append(meal)

    elif command == 'Unlike':
        if guest not in my_dict:
            print(f'{guest} is not at the party.')
        else:
            if meal not in my_dict[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            if meal in my_dict[guest]:
                my_dict[guest].remove(meal)
                print(f"{guest} doesn't like the {meal}.")
                unliked_meals += 1



    line = input()
my_dict = dict(sorted(my_dict.items(),key=lambda x : (-len(x[1]),x[0])))

for key, value in my_dict.items():
    if len(value) > 0 :
        print(f'{key}: {", ".join(value)}')
    else:
        print(f'{key}:')
print(f'Unliked meals: {unliked_meals}')
