from collections import deque

# import sys

# sys.stdin = open('./16173.txt')

            
n = int(input())   
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [1, 0]
dy = [0, 1]

def bfs(x, y, visited):
    que = deque()
    que.append([x, y])
    visited[x][y] = True
    
    while que:
        x, y = que.popleft()
        jmp = graph[x][y]

        if jmp == -1:
            print('HaruHaru')
            return

        for i in range(2):
            nx = x + dx[i] * jmp
            ny = y + dy[i] * jmp

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                que.append([nx, ny])
    print('Hing')

bfs(0, 0, visited)
