number = int(input())
direction = 1
current_size = 0

while (current_size < number and direction == 1) or (direction == - 1 and current_size >0)  :
    current_size += direction
    print("*" * current_size)

    if number == current_size :
        direction = -1