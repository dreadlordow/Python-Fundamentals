users_dict = {}

while True:
    line = input()
    if line == 'End':
        break
    company_name, employee = line.split(' -> ')

    if company_name not in users_dict:
        users_dict[company_name] = []
    if employee not in users_dict[company_name]:
        users_dict[company_name].append(employee)
users_dict = dict(sorted(users_dict.items(), key=lambda x:x[0]))
for company,users in users_dict.items():
    print(f'{company}')
    for user in users:
        print(f'-- {user}')
