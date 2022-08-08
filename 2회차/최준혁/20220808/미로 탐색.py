# from collections import deque

# def bfs(x, y):
#     queue = deque()
#     queue.append((x,y))
#     while queue: # 큐가 빈값이 나올때까지 반복
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[ny][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#     return graph[N-1][M-1]

# N, M = map(int, input().split()) # 행과 열의 입력값
# graph = []

# for i in range(N):
#     # 미로를 한 행씩 넣음(띄워쓰기 없음)
#     graph.append(list(map(int, input())))

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

# print(bfs(0,0))