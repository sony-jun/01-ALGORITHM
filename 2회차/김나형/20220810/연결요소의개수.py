import sys
sys. stdin = open("input.txt")
n, m  = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)

for _ in range(m):
    x, y  = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

def DFS(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            DFS(i)
    # [0, 1, 1, 0, 0, 1, 0]

space = 0 # 구역(연결 요소) 변수        
for j in range(1,n + 1): # 1, 2, 3, 4, 5, 6 의 숫자중 visited에서 1로 변환되지 않은 수가 있다면 함수 실행해주는 조건
    if visited[j] == 0:
        space += 1 # DFS가 실행될 때 마다 +1
        DFS(j)

print(space)
