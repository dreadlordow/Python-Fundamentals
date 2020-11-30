divisor = int(input())
bound = int(input())
number = 0
for n in range (1, bound+1):
    if n % divisor == 0 and n <= bound and n>0 :
        number = n
print(number)