t = int(input())

for i in range(t):

    s = int(input())
    n = int(input())
    if n == 0:
        print(s)
    else:
        for j in range(n):
            q,p = map(int,input().split(' '))
            s += q*p
        print(s)