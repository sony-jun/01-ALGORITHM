import sys
sys.stdin = open("111_연결 요소의 개수_11724.txt", "r")

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph) # [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

def dfs(start):

    visited[start] = 1

    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)

cnt = 0

for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
        
print(cnt)
