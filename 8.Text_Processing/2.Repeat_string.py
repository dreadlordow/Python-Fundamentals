string = input().split()
concatenated_str =''
for word in string:
    length = len(word)
    concatenated_str += (word*length)
print(concatenated_str)