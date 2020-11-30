def get_letter_position_in_alphabet(letter):
    position = 0
    if letter.isupper():
        position = ord(letter) - 64
    else:
        position = ord(letter) - 96

    return position


items = input().split()
sum = 0
for item in items:
    first_letter = item[0]
    last_letter = item[-1]
    number = int(item[1:-1])
    first_letter_position = get_letter_position_in_alphabet(first_letter)
    last_letter_position = get_letter_position_in_alphabet(last_letter)


    if first_letter.isupper():
        sum += (number/first_letter_position)
    else:
        sum += (number*first_letter_position)

    if last_letter.isupper():
        sum -= last_letter_position
    else:
        sum += last_letter_position
print(f'{sum:.2f}')