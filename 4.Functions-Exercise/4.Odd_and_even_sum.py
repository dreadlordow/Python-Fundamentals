def odd_numbers_sum(number):
    even_sum = 0
    odd_sum = 0
    while number > 0 :
        even_or_odd_check = number % 10

        if even_or_odd_check % 2 == 0:
            even_sum += even_or_odd_check
        else :
            odd_sum += even_or_odd_check

        number = int(number/10)
        continue
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'

number = int(input())
result =odd_numbers_sum(number)
print(result)