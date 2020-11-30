start = int(input())
end = int(input())
symbol = ''
separator = ' '
for char in range(start, end+1):
    symbol += (chr(char)+separator)

print(symbol, sep= ' ')