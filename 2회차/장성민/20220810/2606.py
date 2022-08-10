N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
visited[1] = True
stack = [1]

while len(stack) != 0:
    now = stack.pop()

    for adj in graph[now]:
        if not visited[adj]:
            visited[adj] = True
            stack.append(adj)

result = sum(visited) - 1
print(result)

    