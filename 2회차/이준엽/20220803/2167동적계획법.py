### 일반 조건반복

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
mtxs = [list(map(int,input().split())) for i in range(n)]
k = int(input())
result = []
for _ in range(k):
    cordsum = 0
    i,j,x,y = map(int,input().split())
    for p in range(i-1,x):
        for q in range(j-1,y):
            cordsum+=mtxs[p][q]
    result.append(cordsum)
print(*result,sep='\n')

### 동적 계획법####

n,m = map(int,input().split())
mtx = [list(map(int,input().split())) for i in range(n)]

dp = [[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mtx[i-1][j-1]
result = []
k = int(input())
for a in range(k):
    i,j,x,y = map(int,input().split())
    result.append(dp[x][y]-dp[i-1][y]-dp[x][j-1]+dp[i-1][j-1])
print(*result,sep='\n')