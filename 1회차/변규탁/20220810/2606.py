N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()

        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
                
    return discovered

print(len(iterative_dfs(1))-1)