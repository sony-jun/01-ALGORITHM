from collections import deque

dx = [1, -1, 0, 0, 1, -1, -1, 1] # 8방 아래, 위, 오른쪽, 왼쪽,,,
dy = [0, 0, 1, -1, 1, -1, 1, -1]

# 연결된 부분 = 섬

def bfs(a,b):
    queue = deque()
    queue.append((a, b))
    
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    maps = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    island = 0

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and visited[i][j] == False:
                bfs(i,j)
                island += 1
                
    print(island)



