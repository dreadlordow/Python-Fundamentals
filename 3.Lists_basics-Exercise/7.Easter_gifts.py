gifts_input = input().split()
gifts_list = []
for i in gifts_input:
    gifts_list.append(i)

out_of_stock_list = []
required_list = []
command = input().split()
final_list = []
while command[0] != 'No' and command[1] != 'Money':
    type_command = command[0]
    gift = command[1]
    if type_command == 'OutOfStock':
        for n, i in enumerate(gifts_list):
            if i == gift:
                gifts_list[n] = None

    elif type_command == 'Required':
        gift_index = int(command[2])
        index = -1
        for n, i in enumerate(gifts_list):
            index += 1
            if index == gift_index:
                gifts_list[n] = gift

    elif type_command == 'JustInCase' :
        gifts_list[-1] = gift


    command = input().split()

while None in gifts_list:
    gifts_list.remove(None)

for i in gifts_list:
    print(i, end=' ')