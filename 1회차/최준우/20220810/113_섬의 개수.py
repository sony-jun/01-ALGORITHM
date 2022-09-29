# https://www.acmicpc.net/problem/4963
from pprint import pprint
w = -1
h = -1

def dfs(x, y):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    grid[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 1:
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    grid = []
    for _ in range(h):
        # grid = [list(map(int, input().split())) for _ in range(h)]
        grid.append(list(map(int, input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)