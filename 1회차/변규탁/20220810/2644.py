N = int(input())

A, B = map(int, input().split())

M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(start, count):
    discover = []
    stack = [start]
    count = 0
    while stack:
        v = stack.pop()
         
        if v == B:
            print(count)
            break 
        if v not in discover:
            discover.append(v)
            for w in graph[v]:
                stack.append(w)
        count += 1

dfs(A, 0)
