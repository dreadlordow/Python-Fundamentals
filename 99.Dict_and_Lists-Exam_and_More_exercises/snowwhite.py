dwarfs = {}

line = input()
while line != 'Once upon a time':
    name, colour, physics = line.split(' <:> ')
    physics = int(physics)

    if colour not in dwarfs:
        dwarfs[colour] = {}
    if name not in dwarfs[colour]:
        dwarfs[colour].update({name: physics})
    if name in dwarfs[colour]:
        if physics > dwarfs[colour][name]:
            dwarfs[colour][name] = physics

    line = input()
flat_list = []
for k1, v1 in dwarfs.items():
        l = len(v1.keys())
        for k2, v2 in v1.items():
            flat_list.append((v2, l, k1, k2))
flat_list.sort(reverse=True)

for (v2, l, k1, k2) in flat_list:
    print(f'({k1}) {k2} <-> {v2}')