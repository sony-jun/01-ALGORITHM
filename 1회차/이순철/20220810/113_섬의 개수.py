# https://www.acmicpc.net/problem/4963

import sys
sys.stdin = open('_섬의 개수.txt')

# while True:
    # w, h = map(int, input().split())
w = 5;h = 4

# map_ = [input().split() for _ in range(h)]
map_ = [
    ['1', '1', '1', '0', '1'],
    ['1', '0', '1', '0', '1'],
    ['1', '0', '1', '0', '1'],
    ['1', '0', '1', '1', '1']
]

# print(*map_, sep='\n')
cnt = 0
land = 0
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
# 2차원 순회
for x in range(h):
    for y in range(w):
        # if map_[x][y] == 1:
        #     cnt += 1
        # else:
        #     continue
            # 델타값을 이용해 8방향 이동
        print(x, y, end='---')
        print(map_[x][y])               

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
                # 범위 제한과 기준 좌표 재할당
            if 0 <= nx < w and 0 <= ny < h:
                x = nx
                y = ny
            elif 
    # if (w, h) == (0, 0):
    #     print(land)

    #     break
    