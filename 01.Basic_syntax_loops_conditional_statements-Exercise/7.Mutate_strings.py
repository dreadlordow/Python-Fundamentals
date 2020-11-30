first = input()
second = input()
final = ''
some_set = set()
for i in range(len(first)+1):
    final = second[0:i] + first[i::]
    if final not in some_set and not final == first:
        some_set.add(final)
        print(final)