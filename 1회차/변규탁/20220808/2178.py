# N, M = map(int, input().split())
# maps = [list(input()) for _ in range(N)]

# dx = [1, 0, 0, -1]
# dy = [0, 1, -1, 0]
# x, y = 0, 0

# for i in range(N):
#     for j in range(M):

#         for d in range(4):
#             r = i + dx[d]
#             c = j + dy[d]
#             if 0 <= r <= N - 1 and 0 <= c <= M - 1 and maps[r][c] == 1:
#                 if maps[r][c] != 0:
#                     x += 1
#                 elif maps[r][c] != 0:
#                     y += 1

# print(x+y)

from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N-1][M-1]


N, M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))