import re
string = input()


pattern = r'([#]{1}|[\|]){1}([a-zA-Z]+(\s*[a-zA-Z]+))\1([0-9][0-9]/[0-9][0-9]/[0-9][0-9]\1([0-9]+))\1'
matches = re.findall(pattern,string)
matches_to_print = re.finditer(pattern,string)
total_calories = 0

for match in matches:
    total_calories += int(match[4])
days = total_calories // 2000

print(f'You have food to last you for: {days} days!')


for match_to_print in matches_to_print:
    res = re.split(r'#|\|',match_to_print[0])
    product = res[1]
    date = res[2]
    calories = res[3]
    print(f'Item: {product}, Best before: {date}, Nutrition: {calories}')
