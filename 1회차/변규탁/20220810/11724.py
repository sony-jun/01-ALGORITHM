import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


discovered = []
def dfs(start):
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)


cnt = 0
for i in range(1, N + 1):
    if i not in discovered:
        dfs(i)
        cnt += 1

print(cnt)