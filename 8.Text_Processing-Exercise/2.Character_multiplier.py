string_list = input().split()
str_one = string_list[0]
str_two = string_list[1]
len_one = len(str_one)
len_two = len(str_two)
sum = 0

if len_one == len_two:
    for i in range(len_one):
        sum += (ord(str_one[i]) * ord(str_two[i]))
elif len_one > len_two:
    first_str = str_one[0:len_two]
    rem_word = str_one[len_two:]
    for i in range(len_two):
        sum += (ord(first_str[i]) * ord(str_two[i]))
    for i in range(len_one - len_two):
        sum += ord(rem_word[i])

elif len_one < len_two:
    second_str = str_two[0:len_one]
    rem_word = str_two[len_one:]
    for i in range(len_one):
        sum += (ord(second_str[i]) * ord(str_one[i]))
    for i in range(len_two - len_one):
        sum += ord(rem_word[i])


print(sum)