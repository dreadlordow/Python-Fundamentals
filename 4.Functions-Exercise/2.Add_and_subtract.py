def sum_numbers(a,b):
    res = a + b
    return res


def subtract(a,b):
    return a - b

a = int(input())
b = int(input())
c = int(input())

sum = sum_numbers(a, b)
res = sum - c
print(res)
