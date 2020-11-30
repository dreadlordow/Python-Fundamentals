def is_palindrome(word):
    return word == word[::-1]


words = input().split(' ')
search_palindromes = input()

palindromes = [word for word in words if is_palindrome(word)]

print(palindromes)

print(f'Found palindrome {palindromes.count(search_palindromes)} times')
