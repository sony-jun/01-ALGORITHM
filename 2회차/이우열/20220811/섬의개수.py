while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    maps = []
    for _ in range(h):
        maps.append(list(map(int, input().split())))

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                stack = []
                stack.append((i, j))

                while stack:
                    (y, x) = stack.pop()
                    if maps[y][x] == 1:
                        maps[y][x] = 0

                        for k in range(8):
                            ny = y + dy[k]
                            nx = x + dx[k]

                            if -1 < ny < h and -1 < nx < w:
                                if maps[ny][nx] == 1:
                                    stack.append((ny, nx))

                cnt += 1

    print(cnt)
