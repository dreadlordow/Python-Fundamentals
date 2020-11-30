number_of_lines = int(input())
capacity = 255
current_capacity = 0
for i in range(number_of_lines):
    liters_poured = int(input())
    if current_capacity + liters_poured > capacity:
        print(f'Insufficient capacity!')
    else:
        current_capacity += liters_poured
print(f'{current_capacity}')
