factor = int(input())
count = int(input())
empty_list = [factor]
starting_number = factor
for number in range(count-1):
    starting_number += factor
    empty_list.append(starting_number)
print(empty_list)
