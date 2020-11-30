my_dict ={}
languages = []
set_of_languages = set(languages)
language_dict = {}
line = input()

while True:
    if len(line.split()) == 2:
        if line == 'exam finished':
            break
    elif len(line.split('-')) == 2: ##### BAN COMMAND
        token = line.split('-')
        username = token[0]
        if username in my_dict.keys():
            del my_dict[username]

    else: #### SUBMISSION COMMAND
        token = line.split('-')
        username, language, points = token[0], token[1], int(token[2])
        if username not in my_dict:
            my_dict[username] = 0
            my_dict[username] = points
        else:
            if points > int(my_dict[username]):
                my_dict[username] = points
        languages.append(language)
        set_of_languages.add(language)

    line = input()


##### SORTING LANGUAGES
for language_occurance in set_of_languages:
    counter = 0
    for i in sorted(languages):
        if i == language_occurance:
            counter += 1
    language_dict[language_occurance] = counter

#### SORTING AND PRINTING DICTS
language_dict = dict(sorted(language_dict.items(), key=lambda x: (-x[1],x[0])))
my_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1],x[0])))
print(f'Results:')
for key,value in my_dict.items():
    print(f'{key} | {(value)}')
print(f'Submissions:')
for key,value in language_dict.items():
    print(f'{key} - {value}')
