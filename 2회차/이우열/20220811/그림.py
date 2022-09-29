n, m = map(int, input().split())

paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

cnt = 0
area_list = [0]
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            stack = []
            stack.append((i, j))
            area = 0

            while stack:
                (y, x) = stack.pop()
                if paper[y][x] == 1:
                    area += 1
                    paper[y][x] = 0

                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]

                        if -1 < ny < n and -1 < nx < m:
                            if paper[ny][nx] == 1:
                                stack.append((ny, nx))

            cnt += 1
            area_list.append(area)

print(cnt)
print(max(area_list))
