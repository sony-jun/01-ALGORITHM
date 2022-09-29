N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

K = int(input())
for i in range(K):
    ans = 0
    i,j,x,y = map(int, input().split())
    for a in range(i-1, x):
        ans += sum(arr[a][j-1:y])
    print(ans)