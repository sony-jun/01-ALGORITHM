n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def dfs(start):
    stk = [start]
    visited[start] = True

    while stk:
        cur = stk.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stk.append(adj)


dfs(1)

print(visited.count(True) - 1)
