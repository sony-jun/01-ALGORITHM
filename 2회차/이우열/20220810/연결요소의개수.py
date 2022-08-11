import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
stack = []
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0

for i in range(1, n + 1):
    if not visited[i]:
        visited[i] = True
        stack.append(i)
        cnt += 1

        while stack:
            cur = stack.pop()

            for adj in graph[cur]:
                if not visited[adj]:
                    visited[adj] = True
                    stack.append(adj)

print(cnt)
