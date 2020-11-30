line = input()

i = 0
rage_str = ''
result = ""
while i < len(line):
    ch = line[i]

    if ch.isdigit():
        count_str = ch

        if i + 1 < len(line) and line[i+1].isdigit():
            count_str += line[i+1]

        count = int(count_str)
        final_rage = rage_str * count
        result += final_rage
        rage_str = ''
    else:
        rage_str += ch.upper()

    i += 1
# final_string =''
# for char in result:
#     if char.isalpha() and char.islower():
#         final_string += char.upper()
#     else :
#         final_string += char
unique = result
print(f'Unique symbols used: {len(set(unique))}')
print(f'{result}')