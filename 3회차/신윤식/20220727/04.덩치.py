N = int(input())
lst = []

for i in range(N):
    w, h = map(int,input().split())
    lst.append([w,h,1])

for j in range(len(lst)-1):
    for k in range(j+1, len(lst)):
        if lst[j][0] > lst[k][0] and lst[j][1] > lst[k][1]:
            lst[k][2] += 1
        elif lst[j][0] < lst[k][0] and lst[j][1] < lst[k][1]:
            lst[j][2] += 1

for o in lst:
    print(o[2], end=' ')