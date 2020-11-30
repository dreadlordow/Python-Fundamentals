def add_user_to_side(user, side, force_dict):
    if side not in force_dict:
        force_dict[side] = []

    if user not in force_dict.values():
        force_dict[side].append(user)
    return force_dict


force_dict = {}
line = input()
while True:
    if line == 'Lumpawaroo':
        break
    if ' | ' in line:
        side, user = line.split(' | ')
        if side not in force_dict:
            force_dict[side] = []
        all_values = []
        for current_list in force_dict.values():
            all_values += current_list
        if user not in all_values:
            force_dict[side].append(user)

    elif ' -> ' in line:
        user, side = line.split(' -> ')
        old_side = ''
        for key, value in force_dict.items():
            if user in value:
                old_side = key
                break
        if old_side != '':
            force_dict[old_side].remove(user)
            add_user_to_side(user, side, force_dict)
        else:
            add_user_to_side(user, side, force_dict)

        print(f'{user} joins the {side} side!')

    line = input()

force_dict = dict(sorted(force_dict.items(), key=lambda x: (-len(x[1]),x[0]),))
#force_dict = dict(sorted(force_dict.items(), key=lambda x: x[0]))

for key, sorted_list in force_dict.items():
    force_dict[key] = sorted(sorted_list)

for key, values in force_dict.items():
    if len(values) > 0:
        print(f'Side: {key}, Members: {len(values)}')
        for value in values:
            print(f'! {value}')
