### 기본 append 활용

n, m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input())))

delta = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우

stack = []
start = (0,0)
stack.append(start)

while stack:
    y, x = stack.pop(0)
    for i in range(4):
        dy = y + delta[i][0]
        dx = x + delta[i][1]
        if not (0<=dy<n and 0<=dx<m):
            continue
        if graph[dy][dx] != 1:
            continue
        if graph[dy][dx] == 1:
            stack.append((dy,dx))
            graph[dy][dx] = graph[y][x] + 1
print(graph[n-1][m-1])


# ### deque 활용
# from collections import deque

# n, m = map(int,input().split())
# graph = []

# for _ in range(n):
#     graph.append(list(map(int,input())))

# delta = [(-1,0),(1,0),(0,-1),(0,1)]

# stack = deque()
# start = (0,0)
# stack.append(start)

# while stack:
#     y, x = stack.popleft()
#     for i in range(4):
#         dy = y + delta[i][0]
#         dx = x + delta[i][1]
#         if not (0<=dy<n and 0<=dx<m):
#             continue
#         if graph[dy][dx] != 1:
#             continue
#         if graph[dy][dx] == 1:
#             stack.append((dy,dx))
#             graph[dy][dx] = graph[y][x] + 1
# print(graph[n-1][m-1])