import re
n = int(input())
pattern = r'U\$[A-Z][a-z]{2,}U\$P@\$[a-zA-Z]{5,}[0-9]+P@\$'
counter = 0
for i in range(n):
    string = input()
    matches = re.match(pattern, string)
    if matches is not None:
        print(f'Registration was successful')
        match = re.split(r'U\$|P@\$', matches[0])
        print(f'Username: {match[1]}, Password: {match[3]}')
        counter += 1
    else:
        print(f'Invalid username or password')
print(f'Successful registrations: {counter}')