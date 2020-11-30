email = input()

line = input()
while line != 'Complete':
    command = line.split()
    if line  == 'Make Upper':
        email = email.upper()
        print(email)
    elif line == 'Make Lower':
        email = email.lower()
        print(email)

    elif line == 'Encrypt':
        ascii_symbols = [ord(x) for x in email]
        print(*ascii_symbols,sep=' ')

    elif command[0] == 'GetUsername':
        to_print = ''
        if '@' not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            for char in email:
                if char == '@':
                    break
                to_print += char
            print(to_print)

    elif command[0] == 'GetDomain':
        count = int(command[1])
        length = len(email)
        print(email[length-count:length+1])

    elif command[0] == 'Replace':
        to_replace = command[1]
        while to_replace in email:
            for letter in email:
                if letter == to_replace:
                    email = email.replace(letter,'-')
        print(email)

    line = input()