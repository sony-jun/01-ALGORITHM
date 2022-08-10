import sys
sys.stdin = open('바이러스_input.txt')

n = int(input())
m = int(input())

# graph 
graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

# 방문 기록
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
    return print(visited.count(True)-1) 
dfs(1)