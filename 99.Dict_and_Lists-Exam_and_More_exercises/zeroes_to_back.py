list_input = list(map(int, input().split(', ')))
new_list = []
zeroes_counter = 0
for digit in list_input:
    if 0 in list_input:
        list_input.remove(0)
        zeroes_counter+= 1
for i in range(zeroes_counter):
    list_input.append(0)
print(list_input)