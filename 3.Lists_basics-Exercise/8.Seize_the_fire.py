fires = input().split('#')
water = int(input())

effort = 0
total_fire = 0
cell_list = []
print(f'Cells:')
for fire in fires:
    args = fire.split(' = ')
    type = args[0]
    cell = int(args[1])

    if type == 'High' and 81 <= cell <= 125  and water >= cell:
        water -= cell
        effort += 0.25 * cell
        cell_list.append(f" - {cell} ")
        total_fire+=cell

    elif type == 'Medium' and 51 <= cell <= 80 and water >= cell :
        water -= cell
        effort += 0.25 * cell
        cell_list.append(f" - {cell} ")
        total_fire += cell
    elif type == 'Low' and 1 <= cell <= 50 and water >= cell:
        water -= cell
        effort += 0.25 * cell
        cell_list.append(f" - {cell} ")
        total_fire += cell
    else :
        continue

    print(f' - {cell}', end='\n')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')