import re

text = input()
pattern = r'(www\.(([a-zA-Z0-9]+)(-*([a-zA-Z0-9]+))*)((\.[a-zA-Z]+)+))'
while text != '':
    matches = re.finditer(pattern, text)


    for match in matches:
        print(match[0])
    text = input()