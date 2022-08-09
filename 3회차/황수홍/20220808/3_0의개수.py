T = int(input())

for i in range(T):
    n, m = map(int,input().split())
    cnt = 0
    for j in range(n,m+1):
        cnt += str(j).count('0')
    print(cnt)