import sys
sys.stdin = open('연결요소의개수_input.txt')

# 무방향 그래프

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    v1 ,v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
# [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]
# print(graph)
visited = [False] * (n+1)

def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop()
        
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
cnt = 0
for j in range(1,n+1):
    if visited[j] == False:
        cnt += 1
        dfs(j) 

print(cnt)