numberstring = [x for x in input().split()]
sorted_string = sorted(numberstring, key=str)
sorted_string = sorted_string[::-1]
res = ''
for x in sorted_string:
    res+=x
print(int(res))