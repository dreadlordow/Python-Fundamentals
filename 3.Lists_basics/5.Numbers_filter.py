n = int(input())

numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)
command = input()
filtered_numbers = []

for number in numbers :
    if command == 'even' and number % 2 == 0:
        filtered_numbers.append(number)
    elif command == 'odd' and number % 2 != 0 :
        filtered_numbers.append(number)
    elif command == 'negative' and number < 0 :
        filtered_numbers.append(number)
    elif command == 'positive' and number >= 0 :
        filtered_numbers.append(number)
print(filtered_numbers)
