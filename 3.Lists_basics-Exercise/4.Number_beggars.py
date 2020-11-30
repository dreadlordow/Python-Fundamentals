offers = list(map(int,input().split(', ')))
beggars = int(input())

empty_list = []

for i in range(beggars):
    empty_list.append(0)

index = 0

for offer in offers :
    empty_list[index] += offer
    index += 1
    if index == beggars:
        index = 0

print(empty_list)
