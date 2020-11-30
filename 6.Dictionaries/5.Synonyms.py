synonyms = {}

n = int(input())

for _ in range(n):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word, synonyms in synonyms.items():
    factored_synonyms = ', '.join(synonyms)
    print(f'{word} - {factored_synonyms}')