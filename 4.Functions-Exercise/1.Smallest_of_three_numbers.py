def smallest_of_three_numbers(a, b, c) :
    smallest = 0
    if a < b and a < c:
        smallest = a
    if b < a and b < c :
        smallest = b
    if c < a and c < b :
        smallest = c

    return smallest

a = int(input())
b = int(input())
c = int(input())

res = smallest_of_three_numbers(a,b,c)
print(res)