import sys

sys.stdin = open('바이러스.txt')

n = int(input())
m = int(input())

#result_matrix = [[0]*(n+1) for _ in range(n+1)]

graph = [[] for _ in range(n+1)]

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
    #result_matrix[u][v] = 1
    
visited = [False] * (n + 1)
total = 0

visited = [False] * n
def dfs(start):
    stack = [start]
    visited[start] = True
    
    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
            
dfs(1) # 1번 정점에서 시작
#visited[1] = False
print(visited)

 


#무방향 인접 리스트
#[[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]


#유방향 그래프
# [[], [2, 5], [3], [], [7], [2, 6], [], []]

# [[0, 0, 0, 0, 0, 0, 0, 0], 
#  [0, 0, 1, 0, 0, 1, 0, 0], 
#  [0, 0, 0, 1, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0, 0, 0, 1], 
#  [0, 0, 1, 0, 0, 0, 1, 0], 
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0]]

