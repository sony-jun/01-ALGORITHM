import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    cnt = 0

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] == "*":
                    cnt += 1
    return cnt

n = int(input())

maps = [input().rstrip() for _ in range(n)]
maps2 = [input().rstrip() for _ in range(n)]
answer = [["."] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if maps2[i][j] == "x" and maps[i][j] == ".":
            answer[i][j] = bfs(i, j)
        if maps2[i][j] == "x" and maps[i][j] == "*":
            for x in range(n):
                for y in range(n):
                    if maps[x][y] == "*":
                        answer[x][y] = "*"
for i in range(n):
    print("".join(map(str,answer[i])))