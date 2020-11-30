import re
string_input = input()

#emojis_pattern = r'([*|:]{2})([A-Z]{1})([a-z]+)\1'
#emojis_pattern = r'[ |^]([*|:]{2})([A-Z]{1})([a-z]+)\1'
emojis_pattern = r'([:]{2}|[*]{2})[A-Z][a-z]{2,}\1'
numbers_pattern = r'\d'

emojis_matches = re.finditer(emojis_pattern,string_input)
numbers = re.finditer(numbers_pattern, string_input)

emojis_list = []
for element in emojis_matches:
    element = element[0].strip()
    emojis_list.append(element)

numbers_list = []
for num in numbers:
    numbers_list.append(int(num[0]))


threshold = 1
for x in numbers_list:
    threshold = threshold*x

print(f'Cool threshold: {threshold}')
print(f'{len(emojis_list)} emojis found in the text. The cool ones are:')
for emoji in emojis_list:
    char_sum = 0
    for char in emoji:
        if char.isalpha():
            char_sum += ord(char)
    if char_sum > threshold:
        print(f'{emoji}')

