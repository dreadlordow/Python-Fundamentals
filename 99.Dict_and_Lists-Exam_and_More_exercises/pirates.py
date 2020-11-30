
pirates_dict = {}

text = input()
while text != 'Sail':
    args = text.split('||')
    town = args[0]
    people = int(args[1])
    gold = int(args[2])

    if town in pirates_dict.keys():
        pirates_dict[town][0] += (people)
        pirates_dict[town][1] += (gold)
    elif town not in pirates_dict.items():
        pirates_dict[town] = [0,0]
        pirates_dict[town][0]+=(people)
        pirates_dict[town][1]+=(gold)

    text = input()


line = input()
while line != 'End':

    args = line.split('=>')
    command = args[0]
    town = args[1]

    if command == 'Plunder':

        people = int(args[2])
        gold = int(args[3])

        pirates_dict[town][0] -= people
        pirates_dict[town][1] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')

        if pirates_dict[town][0] <= 0 or pirates_dict[town][1] <= 0 :
            del pirates_dict[town]
            print(f'{town} has been wiped off the map!')

    elif command == 'Prosper':
        gold = int(args[2])
        if gold > 0:
            pirates_dict[town][1] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {pirates_dict[town][1]} gold.')
        elif gold < 0 :
            print(f'Gold added cannot be a negative number!')


    line = input()
sorted_dict = dict(sorted(pirates_dict.items(), key=lambda x: (-x[1][1],x[0])))
print(f'Ahoy, Captain! There are {len(sorted_dict.keys())} wealthy settlements to go to:')
for town,values in sorted_dict.items():
    print(f'{town} -> Population: {values[0]} citizens, Gold: {values[1]} kg')