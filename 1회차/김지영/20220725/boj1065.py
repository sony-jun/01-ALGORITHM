x = int(input())
c = 0
for i in range(1,x+1):
    lx = list(map(int,str(i)))
    if i<100:
        c += 1
    elif lx[0]-lx[1] == lx[1]-lx[2]:
            c+=1
print(c)