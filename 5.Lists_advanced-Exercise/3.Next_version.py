mylist = [int(n) for n in input().split('.')]
mylist[2]+=1

if mylist[2] == 10:
    mylist[2] = 0
    mylist[1]+=1
if mylist[1] == 10:
    mylist[1] = 0
    mylist[0]+= 1
print(*mylist, sep='.')