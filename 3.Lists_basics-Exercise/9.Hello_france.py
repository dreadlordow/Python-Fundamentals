items = input().split('|')
budget = int(input())

price_list = []
budget_left = budget
buy = True
profit = 0
money_needed = 150
new_prices = 0

for item in items:
    args = item.split('->')
    clothing_type = args[0]
    price = float(args[1])

    if (clothing_type == 'Clothes' and price > 50.00) or (clothing_type == 'Shoes' and price > 35.00) or (clothing_type == 'Accessories' and price > 20.50):
        buy = False

    else :
        buy = True

    if buy :

        if budget_left >= price :
            selling_price = round(price * 1.4, 2)
            new_prices += selling_price
            profit += selling_price - price
            price_list.append(f'{selling_price:.2f}')

        if budget_left < price :
            price = 0

        budget_left -= price


total_profit = budget_left + new_prices
print(*price_list, sep=' ')
print(f'Profit: {profit:.2f}')

if total_profit >= money_needed:
    print('Hello, France!')
else :
    print('Time to go.')
