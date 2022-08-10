import sys
input = sys.stdin.readline

def dfs(graph, pc, visited):
    visited[pc] = 1
    for i in graph[pc]:
        if visited[i] == 0:
            dfs(graph, i, visited)


n = int(input())
m = int(input())

net = [[] for _ in range(n)]
visited = [0] * n
for _ in range(m):
    v1, v2 = map(int, input().split())
    v1 -= 1
    v2 -= 1
    net[v1].append(v2)
    net[v2].append(v1)

dfs(net, 0, visited)
print(sum(visited)-1)