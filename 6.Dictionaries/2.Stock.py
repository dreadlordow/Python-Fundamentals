data = input()
elements = data.split(' ')
products = {
    elements[index]: int(elements[index+1])
    for index in range(0, len(elements), 2)
}
search_products = input().split(' ')
for search_product in search_products:
    if search_product in products:
        quantity = products[search_product]
        print(f"We have {quantity} of {search_product} left")
    else:
        print(f"Sorry, we don't have {search_product}")