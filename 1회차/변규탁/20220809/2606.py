N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v, discovered = []):
    discovered.append(v)
    for w in graph[v]:
       if w not in discovered:
        discovered = dfs(w, discovered)
    
    return discovered

print(len(dfs(1))-1)

# # stack
# n = int(input())
# m = int(input())
# graph[[] for _ in range(n + 1)]
# visited = [False] * (n+1)
# total = 0

# def dfs(start):
#     stack = [start]
#     visited[start] = True

#     while stack:
#         cur = stack.pop()

#         for adj in graph[cur]:
#             if not visited[adj]:
#                 visited[adj] = True
#                 stack.append(adj)
        