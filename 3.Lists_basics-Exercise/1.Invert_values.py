string = input()
numbers_str = string.split(' ')
numbers = []

for num_str in numbers_str:
    number = -int(num_str)
    numbers.append(number)
print(numbers)
