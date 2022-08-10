n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
stack = []

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited[1] = True
stack.append(1)
cnt = 0

while stack:
    cur = stack.pop()

    for adj in graph[cur]:
        if visited[adj] == False:
            visited[adj] = True
            stack.append(adj)
            cnt += 1

print(cnt)
