import re

pattern = r'[a-zA-Z]+'
participants = input().split(', ')
line = input()
racers = {}
while line != 'end of race':
    name = ''.join(re.findall(pattern, line))
    distance = list([int(x) for x in ''.join(re.findall('\d',line))])
    if name in participants:
        if name not in racers:
            racers[name] = 0
        racers[name] += sum(distance)
    line = input()
racers = dict(sorted(racers.items(),key = lambda x: -x[1]))
places = ['1st place', '2nd place', '3rd place'][::-1]
counter = 0
for key in racers.keys():
    place = places.pop()
    racers[key] = place
    counter += 1
    print(f'{place}: {key}')
    if counter == 3:
        break