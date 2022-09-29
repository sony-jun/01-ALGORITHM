n = int(input())
nlist = list(map(int,input().split(' ')))
lst = [0]*100
s = 0
for i in range(n):
    if lst[nlist[i]] == 1:
        s +=1
    else :
        lst[nlist[i]] = 1
print(s)