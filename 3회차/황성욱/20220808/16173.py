from collections import deque
import sys

sys.stdin = open('./16173.txt')

def bfs(x, y):
    
    queue = deque()
    queue.append([0, 0])
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    dx = [graph[x][y], 0]
    dy = [0, graph[x][y]]
    
    while queue:
        v = queue.popleft() # 0, 0 을 뽑아냅
        
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            print(x, y)
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue            
            
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                x += nx
                y += ny
                
            print(queue, visited)
    
    return visited[n - 1][n - 1]
        
   
            
n = int(input())   
graph = [list(map(int, input().split())) for _ in range(n)]

print(bfs(0, 0))
