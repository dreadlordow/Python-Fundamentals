string = input()
new_str = ''
for char in string:
    new_str += chr(ord(char)+3)
print(new_str)