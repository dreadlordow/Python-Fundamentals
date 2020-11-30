string = input()
numbers_list =[]
non_string = ''

for char in string:
    if char.isdigit():
        numbers_list.append(int(char))
    else:
        non_string += char

take_list = []
skip_list = []

for i in range(len(numbers_list)):
    if i % 2 == 0:
        take_list.append(numbers_list[i])
    else:
        skip_list.append(numbers_list[i])

output = ''

start = 0
current_pos = 0
for k in range(len(take_list)):
    current_pos += take_list[k]

    output += non_string[start:current_pos]
    start = current_pos + skip_list[k]
    current_pos = start

print(output)