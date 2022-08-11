import sys
sys.stdin = open('4963.txt', 'r')
from pprint import pprint

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(i, j):
    for k in range(8):
        nx = i+dx[k]
        ny = j+dy[k]
    if 0 <= nx < h and 0 <= ny < w:
        stack = [(nx,ny)]
        visited[nx][ny] = True

        while stack:
            cur = stack.pop()
            for l in m[cur[0]]:
                if not visited[l]:
                    visited[l] = True
                    stack.append(l)

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    m = [list(map(int,input().split())) for _ in range(h)]
    cnt = 0
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if m[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)




