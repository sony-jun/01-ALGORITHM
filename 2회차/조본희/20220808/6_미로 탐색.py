import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(N)]
route = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = [(0, 0)]
route[0][0] = 1

while queue:
    x, y = queue.pop(0)

    if x == N-1 and y == M-1:
        print(route[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if route[nx][ny] == 0 and maze[nx][ny] == 1:
                route[nx][ny] = route[x][y] + 1
                queue.append((nx,ny))
    print(route)