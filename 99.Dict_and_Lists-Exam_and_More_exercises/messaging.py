number_string = input().split()
string = input()
string_list = []
for el in string:
    string_list.append(el)
word = ''
break_flag = False
for element in number_string :
    sum = 0
    counter = -1
    for string_digit in element:
        digit = int(string_digit)
        sum += digit

    while counter != sum :
        for letter in string_list:
            counter += 1
            if counter == sum:
                word += letter
                string_list.remove(letter)
                break_flag = True
                break
        if break_flag:
            break

print(word)