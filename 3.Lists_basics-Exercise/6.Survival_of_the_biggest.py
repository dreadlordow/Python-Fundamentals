import sys
numbers_string = input().split()
removed = int(input())
numbers_list = []

counter = 0
string_to_int_number = 0
for number in numbers_string:
    string_to_int_number = int(number)
    numbers_list.append(string_to_int_number)
for _ in range(removed):
    min_number = sys.maxsize
    for i in numbers_list:
        if min_number > i:
            min_number = i
    numbers_list.remove(min_number)
    counter +=1
    if counter == removed:
        break

print(numbers_list)