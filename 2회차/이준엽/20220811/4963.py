# import sys
# read = sys.stdin.readline
# sys.setrecursionlimit(100000)

# delta = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
# def dfs(i,j):
#     while stack:
#         start = stack.pop()
#         i = start[0]
#         j = start[1]
#         for d in range(8):
#             d_i = i+delta[d][0]
#             d_j = j+delta[d][1]
#             if 0<=d_i<h and 0<=d_j<w:
#                 if maps[d_i][d_j] == 1 and visited[d_i][d_j] == False:
#                     stack.append((d_i,d_j))
#                     visited[d_i][d_j] = True
#                     dfs(i,j)
# while True:
#     cnt = 0
#     w,h = list(map(int,input().split()))
#     if w == 0 and h == 0:
#         break
#     maps = [list(map(int,input().split())) for i in range(h)]
#     visited = [list(False for i in range(w)) for i in range(h)]
#     stack = []

#     for i in range(h):
#         for j in range(w):
#             if maps[i][j] == 1 and visited[i][j] == False:
#                 visited[i][j] = True
#                 stack.append((i,j))
#                 dfs(i,j)
#                 cnt+=1
#     print(cnt) 


import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
  dx = [1, 1, -1, -1, 1, -1, 0, 0]
  dy = [0, 1, 0, 1, -1, -1, 1, -1]

  field[x][y] = 0
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
      dfs(nx, ny)

while True:
  w, h = map(int, read().split())
  if w == 0 and h == 0:
    break
  field = []
  count = 0
  for _ in range(h):
    field.append(list(map(int, read().split())))
  for i in range(h):
    for j in range(w):
      if field[i][j] == 1:
        dfs(i, j)
        count += 1
  
  print(count)