usernames = input().split(', ')
valid_usernames = []

for username in usernames:
    is_valid = False
    for char in username:
        if 3 <= len(username) <= 16 and (char.isalpha() or char.isdigit() or char == '-' or char == '_') :
            is_valid = True
        else:
            is_valid = False
            break
    if is_valid:
        valid_usernames.append(username)
print('\n'.join(valid_usernames))