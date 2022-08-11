import sys
sys.stdin = open("8. 섬의 개수.txt", "r")
from collections import deque

while True:
    m, n = map(int,input().split())
    island = [list(map(int,input().split())) for _ in range(n)]
    if m == 0 and n == 0:
        break
    # 우 왼 아 위 왼위 오위 오아 왼아
    q = deque()
    cnt = 0
    dx = [0,0,1,-1,-1,-1,1,1]
    dy = [1,-1,0,0,-1,1,1,-1]
    for i in range(n):
        for j in range(m):
            if island[i][j] == 1:
                q.append((i,j))
                island[i][j] = 2
                
                while q:
                    # 현재 위치를 q에서 꺼내주고
                    cx, cy = q.popleft()
                    # 8방향 탐색을 해준다.
                    for k in range(8):
                        nx = cx + dx[k]
                        ny = cy + dy[k]
                        # 전체 배열 범위 안에 있으면서
                        if 0 <= nx < n and 0 <= ny < m:
                            # 육지이면 값을 2로 바꿔주고 q에 넣어준다.
                            if island[nx][ny] == 1:
                                q.append((nx, ny))
                                island[nx][ny] = 2

                # 이어져 있는 육지를 다 돌았다면 cnt+1
                else:
                    cnt += 1

    print(cnt)