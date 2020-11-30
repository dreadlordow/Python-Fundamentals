shops = input().split()
n = int(input())

for i in range(n):
    line = input()
    args = line.split()
    command = args[0]
    length = len(shops)
    if command == 'Include':
        shop = args[1]
        shops.append(shop)

    elif command == 'Visit':
        criteria = args[1]
        number_of_shops = int(args[2])

        if length >= number_of_shops:
            if criteria == 'first':
                shops = shops[number_of_shops:]
            elif criteria == 'last':
                shops = shops[:length-number_of_shops]

    elif command == 'Prefer':
        shop_index_one = int(args[1])
        shop_index_two = int(args[2])
        if 0 <= shop_index_one < length and 0 <= shop_index_two < length:
            shops[shop_index_one], shops[shop_index_two] = shops[shop_index_two], shops[shop_index_one]

    elif command == 'Place' :
        shop = args[1]
        index = int(args[2])
        if index+1 <= length:
            shops.insert(index+1, shop)

print(f'Shops left:')
print(' '.join(shops))