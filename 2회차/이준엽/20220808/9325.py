t = int(input())
for _ in range(1,t+1):
    s = int(input())
    n = int(input())
    for i in range(n):
        q,p = map(int,input().split())
        s+=q*p
    print(s)