import re
n = int(input())
pattern = r'^\|[A-Z]+\|:#[a-zA-Z]+ [a-zA-Z]+#$'

for _ in range(n):
    line = input()
    matches = re.match(pattern,line)
    if matches is not None:
        match = re.split('\||:|#', line)
        name = match[1]
        title = match[4]
        print(f'{name}, The {title}')
        print(f'>> Strength: {len(name)}')
        print(f'>> Armour: {len(title)}')
    else:
        print(f'Access denied!')