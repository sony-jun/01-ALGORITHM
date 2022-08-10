while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:                   # w, h가 모두 0이면 종료
        break

    maps = [list(map(int, input().split())) for _ in range(h)]

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]        # 델타 탐색을 위한 8방위 좌표
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    cnt = 0                                 # 섬의 개수

    def dfs(i, j):                          # DFS 시작
        stack = []
        stack.append((i, j))                # 시작 위치를 스택에 넣어준다

        while stack:
            (y, x) = stack.pop()            # 스택에서 위치를 꺼낸 뒤
            maps[y][x] = 0                  # 땅이었던 위치를 바다로 바꾸어준다
            # 이미 탐색을 마쳤기 때문
            for k in range(8):              # 8방위 좌표를 모두 탐색하며
                ny = y + dy[k]
                nx = x + dx[k]

                if -1 < ny < h and -1 < nx < w:     # 범위에서 벗어나지 않고
                    if maps[ny][nx] == 1:           # 땅이라면
                        stack.append((ny, nx))      # 스택에 추가한다

        return 1                            # 하나의 섬을 완성했으므로 1을 리턴한다

    for i in range(h):
        for j in range(w):                  # 모든 지도를 순회하며
            if maps[i][j] == 1:             # 지도에서 땅인 위치에서 시작
                cnt += dfs(i, j)            # 섬의 개수를 누적한다

    # print(f'섬의 개수 {cnt}')
    print(cnt)
