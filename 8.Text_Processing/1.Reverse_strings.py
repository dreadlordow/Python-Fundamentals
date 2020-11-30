def reverse(string):
    return string[::-1]

string = input()
words = []
while string != 'end':
    words.append(string)
    string = input()

for word in words:
    print(f'{word} = {reverse(word)}')