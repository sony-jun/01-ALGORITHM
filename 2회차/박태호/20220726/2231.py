n = int(input()) #분해합 216
re = 0
for i in range(1,n+1): #1~216 
    a = list(map(int, str(i))) #198
    re = i+sum(a)
    if re == n:
        print(i)
        break
    if i==n:
        print(0)