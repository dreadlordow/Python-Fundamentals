import re

pattern = r'^%(?P<name>[A-Z]{1}[a-z]+)%[^%$\.\|]*<(?P<product>\w+)>[^%$\.\|]*\|(?P<quantity>\d+)\|[^|$%.]*?(?P<price>\d+\.*\d*)\$'
string = input()
total_income = 0
while string != 'end of shift':
    matches = re.match(pattern, string)

    if matches is not None:
        cost = int(matches.group('quantity')) * float(matches.group('price'))
        print(f'{matches.group("name")}: {matches.group("product")} - {cost:.2f}')
        total_income += cost

    string = input()
print(f'Total income: {total_income:.2f}')