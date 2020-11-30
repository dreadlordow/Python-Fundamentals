def add_to_password_dict(contest, password, passwords_dict):
    if contest not in passwords_dict.items():
        passwords_dict[contest] = password

    return passwords_dict


def add_to_contest_dict(submissions, contest_dict, passwords_dict):
    args = submissions.split('=>')
    lang = args[0]
    passwrd = args[1]
    username = args[2]
    points = int(args[3])
    is_add_to_contests = False
    if lang in passwords_dict.keys():
        if passwords_dict[lang] == passwrd:
            is_add_to_contests = True
    if is_add_to_contests:
        if username not in contest_dict.keys():
            contest_dict[username] = {}
        if username in contest_dict.keys():
            if lang in contest_dict[username]:
                if contest_dict[username][lang] < points:
                    contest_dict[username][lang] = points
                    return contest_dict
            elif lang not in contest_dict[username]:
                contest_dict[username][lang] = points


    return contest_dict


passwords_dict = {}
line_contest = input()
while line_contest != 'end of contests':
    tokens = line_contest.split(':')
    contest = tokens[0]
    password = tokens[1]
    add_to_password_dict(contest, password, passwords_dict)

    line_contest = input()


contest_dict = {}
while True :
    submissions = input()
    if submissions == 'end of submissions':
        break
    add_to_contest_dict(submissions, contest_dict, passwords_dict)
points_dict = {}
max_points = 0
best_contestant = ''
for contestant in contest_dict.keys():
    current_contestant_points = 0
    for points in contest_dict[contestant].values():
        current_contestant_points += points
    if current_contestant_points > max_points:
        max_points = current_contestant_points
        best_contestant = contestant
points_dict[best_contestant] = max_points


contest_dict = {letter: {contest: score

    for contest, score in
        sorted(sub_dict.items(), key=lambda val: val[1], reverse=True)

         } for letter, sub_dict in sorted(contest_dict.items(), key=lambda val: val[0])
}

for k,v in points_dict.items():
    print(f'Best candidate is {k} with total {v} points.')
print(f'Ranking:')
for username,data in contest_dict.items():
    print(f'{username}')
    for field, points in data.items():
        print(f'#  {field} -> {points}')