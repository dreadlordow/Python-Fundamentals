def is_palindrome(text):
    is_palindrome = True
    for i in text :
        if text != text[::-1]:
            is_palindrome = False
        else :
            is_palindrome = True


    return is_palindrome


def palindrom_check(input) :
    for element in input:
        print(is_palindrome(element))



input = input().split(', ')
palindrom_check(input)
