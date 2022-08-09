T = int(input())

for i in range(T):
    s = int(input())
    n = int(input())
    sum = 0
    for j in range(n):
        q, p = map(int,input().split())
        sum += (q * p)
    print(sum+s)