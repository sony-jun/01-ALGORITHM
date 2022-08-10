from re import L
import sys
sys. stdin = open("input.txt")
n = int(input())
r1, r2 = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
res = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    # [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]
def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            res[i] = res[v] + 1
            dfs(i)
dfs(A)

if res[B]>0:
    print(res[B])
else:
    print(-1)

DFS(1)
print(sum(visited)-1)

        
