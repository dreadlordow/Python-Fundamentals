words = input().split(', ')
text = input()
lst = []
for word in words:
    if word in text:
        lst.append(word)
print(lst)