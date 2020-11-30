initial_health = 100
initial_bitcoins = 0
current_health = initial_health
rooms = input().split('|')
room_counter = 0
for element in rooms:
    room = element.split()
    command = room[0]
    amount = int(room[1])

    if command == 'potion':
        current_health += amount
        ammount_healed = amount - (current_health - 100)
        if current_health > 100:
            ammount_healed = amount - (current_health - 100)
            current_health = 100
        else:
            ammount_healed = amount
        print(f'You healed for {ammount_healed} hp.')
        print(f'Current health: {current_health} hp.')
    elif command == 'chest':
        print(f'You found {amount} bitcoins.')
        initial_bitcoins += amount
    else:
        current_health -= amount
        if current_health > 0:
            print(f'You slayed {command}.')
        else:
            print(f'You died! Killed by {command}.')


    room_counter += 1
    if current_health == 0:
        break
if current_health > 0 :
    print(f"You've made it!")
    print(f'Bitcoins: {initial_bitcoins}')
    print(f'Health: {current_health}')
else :
    print(f'Best room: {room_counter}')