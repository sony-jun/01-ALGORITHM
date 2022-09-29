# 미로 미해결
N, M = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
cnt = 1
while M > y >= 0 and N > x >= 0 and x != N and y != M:
    for a in range(4):
        if miro[x + dx[a]][y + dy[a]] == 1:
            save = a
            cnt += 1
            x += dx[a]
            y += dy[a]