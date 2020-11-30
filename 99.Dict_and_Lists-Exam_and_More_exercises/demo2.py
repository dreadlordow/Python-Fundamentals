def data_type_reader(data_type, some_input):
    if data_type == 'int':
        some_input = f'{float(some_input)*2:.0f}'
    elif data_type == 'real':
        some_input = f'{float(some_input)*1.5:.2f}'
    else :
        some_input = f'${some_input}$'
    return some_input

data_type = input()
some_input = input()
some_input = data_type_reader(data_type,some_input)
print(some_input)