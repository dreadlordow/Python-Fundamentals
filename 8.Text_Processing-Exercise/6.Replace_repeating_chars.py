string = input()
new_str = ''
for i in range(len(string)):
    ch = string[i]

    if i + 1 == len(string) or ch != string[i+1]:
        new_str += ch
print(new_str)