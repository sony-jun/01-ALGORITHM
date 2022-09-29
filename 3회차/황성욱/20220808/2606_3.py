from collections import deque
import sys

sys.stdin = open('./2606.txt')
def bfs(graph, start, visited):
    que = deque([start])
    visited[start] = True
    cnt = 0
    while que:
        v = que.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                que.append(i)
                cnt += 1
    return cnt


n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    adj[x].append(y) 
    adj[y].append(x)

print(bfs(adj, 1, visited))
