substring = input()
string = input()

while substring in string:
    string = string.replace(substring, '')

    if substring not in string:
        break
print(string)