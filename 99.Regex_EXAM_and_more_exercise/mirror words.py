import re
string = input()
words = []
mirror_words = []
pattern = r'(#|@)[a-zA-Z]{3,}\1{2}[a-zA-Z]{3,}\1'

matches = re.finditer(pattern, string)

for match in matches:

    split_match = re.split('@|#|@@|##', match[0])
    word_one = split_match[1]
    word_two = split_match[3]
    words.append(word_one)
    if word_one == word_two[::-1]:
        mirror_words.append(f'{word_one} <=> {word_two}')

if len(words) == 0:
    print(f'No word pairs found!')
else:
    print(f'{len(words)} word pairs found!')
if len(mirror_words) == 0:
    print(f'No mirror words!')

else:

    print(f'The mirror words are:')
print(f', '.join(mirror_words))