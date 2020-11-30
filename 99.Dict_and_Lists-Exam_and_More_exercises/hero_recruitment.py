line = input()
my_dict = {}
while line != 'End':
    args = line.split()
    command = args[0]
    hero = args[1]
    if command == 'Enroll':
        if hero not in my_dict.keys():
            my_dict[hero] = []
        elif hero in my_dict.keys():
            print(f'{hero} is already enrolled.')

    elif command == 'Learn':
        spell = args[2]
        if hero not in my_dict.keys():
            print(f"{hero} doesn't exist.")
        elif spell in my_dict[hero]:
            print(f'{hero} has already learnt {spell}.')
        else:
            my_dict[hero].append(spell)

    elif command == 'Unlearn':
        spell = args[2]
        if hero not in my_dict.keys():
            print(f"{hero} doesn't exist.")
        elif spell not in my_dict[hero]:
            print(f"{hero} doesn't know {spell}.")
        else:
            my_dict[hero].remove(spell)
    line = input()
my_dict = dict(sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0])))
print(f'Heroes:')

# for key in my_dict.keys():
#     print(f'== {key}:',end=' ')
#     if len(my_dict[key]) > 0:
#         for item in my_dict.values():
#             print(' '.join(item))
for key, item in my_dict.items():
    print(f"== {key}: {' '.join(item)}")