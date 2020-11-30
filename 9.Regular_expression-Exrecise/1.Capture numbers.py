import re

pattern = '\d+'

while True:
    text = input()

    if not text:
        break

    res = re.findall(pattern,text)

    for rez in res:
        print(rez, end=' ')