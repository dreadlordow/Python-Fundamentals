first_row = list(map(int, input().split()))
second_row = list(map(int, input().split()))
third_row = list(map(int, input().split()))
result = first_row + second_row + third_row

if result[0] == result[1] == result[2] :
    if result[0] == 1:
        print(f'First player won')
    elif result[0] == 2 :
        print(f'Second player won')
elif result[3] == result[4] == result[5]:
    if result[3] == 1:
        print(f'First player won')
    elif result[3] == 2:
        print(f'Second player won')
elif result[6] == result[7] == result[8]:
    if result[6] == 1:
        print(f'First player won')
    elif result[6] == 2:
        print(f'Second player won')
elif result[0] == result[4] == result[8]:
    if result[0] == 1:
        print(f'First player won')
    elif result[0] == 2:
        print(f'Second player won')
elif result[2] == result[4] == result[6] :
    if result[2] == 1:
        print(f'First player won')
    elif result[2] == 2:
        print(f'Second player won')
elif result[0] == result[3] == result [6] :
    if result[0] == 1:
        print(f'First player won')
    elif result[0] == 2:
        print(f'Second player won')
elif result[2] == result[5] == result[8]:
    if result[2] == 1:
        print(f'First player won')
    elif result[2] == 2:
        print(f'Second player won')
elif result[1] == result[4] == result[7]:
    if result[1] == 1:
        print('First player won')
    elif result[1] == 2:
        print(f'Second player won')

else :
    print('Draw!')
