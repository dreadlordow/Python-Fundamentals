import re
n = int(input())

to_count = ['s','t','a','r','S','T','A','R']
pattern = r'@(?P<planet>[a-zA-Z]+)[^@\-!:>]*:(?P<population>[0-9]+)[^@\-!:>]*!(?P<attack_type>[A|D])![^@\-!:>]*->(?P<soldiers>[0-9]+)'
planets = {'Attacked planets':[], 'Destroyed planets': []}
for _ in range(n):
    count = 0
    string = input()
    decrypted = ''
    for char in string:
        if char in to_count:
            count += 1
    for char in string:
        decrypted += chr(ord(char) - count)
    matches = re.search(pattern,decrypted)
    if matches is not None:
        planet = matches.group('planet')
        population = int(matches.group('population'))
        attack_type = matches.group('attack_type')
        soldiers = int(matches.group('soldiers'))
        if attack_type == 'A':

            planets['Attacked planets'].append(planet)

        elif attack_type == 'D':

            planets['Destroyed planets'].append(planet)



for key in planets.keys():
    planets[key] = sorted(planets[key])
    print(f'{key}: {len(planets[key])}')
    for value in planets[key]:
        print(f'-> {value}')