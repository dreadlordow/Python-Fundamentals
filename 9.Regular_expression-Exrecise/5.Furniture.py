import re
line = input()
to_match = []
pattern = r'>>([a-zA-Z]+)<<([0-9]+[.[0-9]+]*)!([0-9]+)'
while line != 'Purchase':
    to_match.append(line)

    line = input()

total = 0
print(f'Bought furniture:')
for match in to_match:
    something = re.findall(pattern,match)
    if len(something) == 0:
        continue
    if len(something) > 0:
        total += (float(something[0][1])*float(something[0][2]))
        print(f'{something[0][0]}')
print(f'Total money spend: {total:.2f}')