word = input()

my_dict = {}
skip_char = ' '
for char in word:
    if char is not skip_char:
        if char not in my_dict:
            my_dict[char] = 0
        my_dict[char] += 1

for key,value in (my_dict.items()):
    print(f'{key} -> {value}')