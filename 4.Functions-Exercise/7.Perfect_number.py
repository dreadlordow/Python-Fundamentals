def number_divisors(number):
    is_divisor = False
    for i in range(number-1, 0, -1):
        if number % i == 0 :
            number_int = int(i)
            divisors_list.append(number_int)

    divisor_sum = sum(divisors_list)
    if divisor_sum == number:
        return 'We have a perfect number!'
    else :
        return "It's not so perfect."



divisors_list = []
number = int(input())
result = number_divisors(number)
print(result)

