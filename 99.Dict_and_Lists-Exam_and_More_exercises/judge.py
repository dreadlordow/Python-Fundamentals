contest_dict = {}
points_dict = {}
command = input()

while command != 'no more time':
    username, contest, points = command.split(' -> ')
    points = int(points)

    if contest not in contest_dict:
        contest_dict[contest] = {}
    if username not in contest_dict[contest].keys():
        contest_dict[contest][username] = points



    elif username in contest_dict[contest]:
        if contest_dict[contest][username] < points:
            contest_dict[contest][username] = points


    command = input()

for contest,values in contest_dict.items():
    for username,points in values.items():
        if username not in points_dict:
            points_dict[username] = 0
        points_dict[username] += points

for key,value in contest_dict.items():
    contest_dict[key] = dict(sorted(value.items(),key=lambda x: (-x[1],x[0])))

for key in contest_dict.keys():
    print(f'{key}: {len(contest_dict[key].keys())} participants')
    i = 1
    for user,points in contest_dict[key].items():
        print(f'{i}. {user} <::> {points}')
        i += 1
print(f'Individual standings:')
j = 1
points_dict = dict(sorted(points_dict.items(),key=lambda x: (-x[1],x[0])))
for k,v in points_dict.items():
    print(f'{j}. {k} -> {v}')
    j += 1