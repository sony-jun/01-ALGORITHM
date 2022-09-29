from collections import deque

dx = [1, -1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1  # 시작위치도 카운트 

    while queue:
        x, y = queue.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
    
    return visited[N-1][M-1] # 항상 도착 위치로 이동하는 경우만 있기 때문에 마지막 인덱스를 출력하는것..

N, M = map(int, input().split())

miro = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

print(bfs())

# WoW..
