materials_dict = {}

line = input().split()
motes = 'motes'
shards = 'shards'
fragment = 'fragments'
is_finished = False
while True:
    for i in range(0, len(line), 2):
        resource = line[i+1].lower()
        if resource not in materials_dict:
            materials_dict[resource] = 0
        materials_dict[resource] += int(line[i])

        if motes in materials_dict:
            if materials_dict[motes] >= 250:
                materials_dict[motes] -= 250
                print(f'Dragonwrath obtained!')
                is_finished = True
                break
        else :
            materials_dict[motes] = 0
        if shards in materials_dict:
            if materials_dict[shards] >= 250:
                materials_dict[shards] -= 250
                print(f'Shadowmourne obtained!')
                is_finished = True
                break
        else :
            materials_dict[shards] = 0
        if fragment in materials_dict :
            if materials_dict[fragment] >= 250:
                materials_dict[fragment] -= 250
                print(f'Valanyr obtained!')
                is_finished = True
                break
        else :
            materials_dict[fragment] = 0
    if is_finished:
        break


    line = input().split()


key_materials = {key:val for key,val in materials_dict.items() if key == 'shards' or key == 'motes' or key == 'fragments'}
junk_materials = {key:val for key,val in materials_dict.items() if key != 'shards' and key != 'motes' and key != 'fragments'}

res = {k: v for k, v in sorted(key_materials.items(), key=lambda item: (-item[1], item[0]))}
junk_res = {k: v for k,v in sorted(junk_materials.items(), key=lambda item: item[0])}

for k, v in res.items():
    print(f'{k}: {v}')
for k, v in junk_res.items():
    print(f'{k}: {v}')
