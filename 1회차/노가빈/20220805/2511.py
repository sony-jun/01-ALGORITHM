alist = list(map(int,input().split(' ')))
blist = list(map(int,input().split(' ')))
countlist = []
acount = 0
bcount = 0
countTrue = 0
for i in range(10):
    if alist[i] > blist[i]:
        acount += 3
        countTrue = i
    elif blist[i] > alist[i]:
        bcount += 3
        countTrue = i
    else:
        acount +=1
        bcount +=1
print(acount,bcount)
if acount == bcount:
    if countTrue == 0:
        print('D')
    else:
        if alist[countTrue] > blist[countTrue]:
            print('A')
        elif blist[countTrue] > alist[countTrue]:
            print('B')
else:
     print('A' if acount> bcount else 'B')      
    
