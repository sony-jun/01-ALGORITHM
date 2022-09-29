def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        now = stack.pop()
        for adj in graph[now]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)

result = 0
for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        result += 1

print(result)