number_of_integers = int(input())
sum = 0
for i in range(number_of_integers):
    character = input()
    character_to_number = ord(character)
    sum += character_to_number
print(f'The sum equals: {sum}')

