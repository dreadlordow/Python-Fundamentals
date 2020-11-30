def plant_name_check(plant_name, plant_dict):
    if plant_name in plant_dict:
        return True
    return False


plant_dict = {}
n = int(input())

for _ in range(n):
    plant, rarity = input().split('<->')
    if plant not in plant_dict.keys():
        plant_dict[plant] = [0, []]  # First element is rarity, Second element is list containing rating
    plant_dict[plant][0] = int(rarity)

while True:
    cmd = input()
    if cmd == 'Exhibition':
        break

    cmd = cmd.replace(':', ' -')
    args = cmd.split(' - ')
    command = args[0]
    plant_name = args[1]
    rating_as_var = plant_dict[plant_name][1]

    if command == 'Rate':
        rating = int(args[2])
        if plant_name_check(plant_name, plant_dict):
            plant_dict[plant_name][1].append(rating)
        else:
            print('error')

    elif command == 'Update':
        new_rarity = int(args[2])
        if plant_name_check(plant_name, plant_dict):
            plant_dict[plant_name][0] = new_rarity
        else:
            print('error')

    elif command == 'Reset':
        if plant_name_check(plant_name, plant_dict):
            plant_dict[plant_name][1].clear()
        else:
            print('error')
    print(rating_as_var)
for plant in plant_dict.keys():  # Summing average ratings
    if len(plant_dict[plant][1]) > 0:
        plant_dict[plant][1] = sum(plant_dict[plant][1])/len(plant_dict[plant][1])
    else:
        plant_dict[plant][1] = 0

plant_dict = dict(sorted(plant_dict.items(),key=lambda x:(x[1][0], x[1][1]),reverse=True))
print('Plants for the exhibition:')

for k, v in plant_dict.items():
    print(f'- {k}; Rarity: {v[0]}; Rating: {v[1]:.2f}')