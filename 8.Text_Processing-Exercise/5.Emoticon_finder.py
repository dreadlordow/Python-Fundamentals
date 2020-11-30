string = input()

for i in range(len(string)):
    if i+1 < len(string):
        if string[i] == ':':
            str_to_print = string[i] + string[i+1]
            print(str_to_print)
