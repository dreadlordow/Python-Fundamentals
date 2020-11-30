products_dict = {}

while True:
    line = input()
    if line == 'buy':
        break
    name, price, quantity = line.split()
    total =[float(price), float(quantity)]
    if name not in products_dict:
        products_dict[name] = [0, 0]
    products_dict[name][0] = total[0]
    products_dict[name][1] += total[1]

for product, total_price in products_dict.items():
    print(f'{product} -> {total_price[0]*total_price[1]:.2f}')

