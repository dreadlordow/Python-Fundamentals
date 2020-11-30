n = int(input())
word = input()
string = []

for _ in range(n):
    sentence = input()

    string.append(sentence)
string_with_word = []
for j in string :
    if word in j :
        string_with_word.append(j)
print(string)
print(string_with_word)