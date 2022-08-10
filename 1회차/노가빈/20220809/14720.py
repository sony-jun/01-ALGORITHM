n = int(input())
lst = list(map(int,input().split(' ')))
c = 0
for i in range(n):
    try:
        if lst[i] == 0:
            c += 1
            if lst[i+1] == 1:
                c += 1
                if lst[i+2] == 2:
                    c += 1
    except:
        continue
print(c)
