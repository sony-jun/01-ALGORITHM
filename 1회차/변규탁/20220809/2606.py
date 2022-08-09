N = int(input())
M = int(input())

graph = [[]*N for _ in range(N+1)]
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