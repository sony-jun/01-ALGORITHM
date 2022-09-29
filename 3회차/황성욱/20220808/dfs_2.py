import sys

sys.stdin = open('./2606.txt')
cnt = 0
def dfs(graph, v, visted):
    global cnt
    visted[v] = True
    for i in graph[v]:
        if not visted[i]:
            dfs(graph, i, visted)
            cnt += 1
    return cnt
n = int(input())
m = int(input())
graph = [[]]
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

print(dfs(adj, 1, visited))