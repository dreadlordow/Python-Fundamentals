n = int(input())
my_dict = {}
for i in range(n):
    car_input = input().split('|')
    add_car = car_input[0]
    add_mileage = int(car_input[1])
    add_fuel = int(car_input[2])
    my_dict[add_car] = [add_mileage, add_fuel]

line = input()
while line != 'Stop':
    args = line.split(' : ')
    command = args[0]
    car = args[1]

    if command == 'Drive':
        distance = int(args[2])
        fuel = int(args[3])

        if fuel > my_dict[car][1]:
            print(f'Not enough fuel to make that ride')
        else :
            my_dict[car][0] += distance
            my_dict[car][1] -= fuel
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if my_dict[car][0] >= 100000:
            del my_dict[car]
            print(f'Time to sell the {car}!')
    elif command == 'Refuel':
        fuel = int(args[2])
        max_fuel = 75

        if fuel + my_dict[car][1] > max_fuel:
            fuel_to_add = fuel - ((fuel + my_dict[car][1]) - max_fuel)
            my_dict[car][1] = max_fuel
        else:
            my_dict[car][1] += fuel
            fuel_to_add = fuel
        print(f'{car} refueled with {fuel_to_add} liters')

    elif command == 'Revert':
        kilometers = int(args[2])
        my_dict[car][0] -= kilometers
        if my_dict[car][0] < 10000:
            my_dict[car][0] = 10000
        else :
            print(f'{car} mileage decreased by {kilometers} kilometers')

    line = input()

my_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1][0],x[0])))

for key,value in my_dict.items():
    print(f'{key} -> Mileage: {my_dict[key][0]} kms, Fuel in the tank: {my_dict[key][1]} lt.')