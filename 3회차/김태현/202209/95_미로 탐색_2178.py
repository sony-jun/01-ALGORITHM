from pprint import pprint
from collections import deque
import sys
sys.stdin = open("95_미로 탐색_2178.txt", "r")

# BFS 탐색
# 다음 경로로 진행할 때마다 += 1
# 도착 좌표에 도달하면 종료

n, m = map(int, input().split())

# 그래프 생성 후 input 값 받음
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 델타 탐색 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        (x, y) = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[n-1][m-1]

print(BFS(0, 0))