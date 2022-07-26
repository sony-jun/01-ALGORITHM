n = int(input())
re = 0
for i in range(1,n+1): #1~216
    a = list(map(int, str(i)))
    re = i+sum(a)
    if re == n:
        print(i)
        break
    if i==n:
        print(0)