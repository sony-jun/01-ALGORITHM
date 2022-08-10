from sys import stdin
input = stdin.readline

N, M = map(int,input().split())

def dfs(start, depth): #깊이 탐색
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth+1)

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
            visited[i] = True
        else:
            dfs(i, 0)
            cnt += 1
print(cnt)