# https://www.acmicpc.net/problem/2644

# 촌수 찾기

import sys
sys.stdin = open("2644.txt")

N = int(input())
A, B = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())  
    graph[x].append(y)
    graph[y].append(x)

visit = [0] * (N+1)

result = []
def dfs(v, num):
    num += 1
    visit[v] = 1

    if v == B:
        result.append(num)

    for i in graph[v]:
        if not visit[i]:
            dfs(i, num)
          
dfs(A, 0)

if len(result) == 0:
    print(-1)

else:
    print(result[0] - 1)